#!/usr/bin/env python3
"""Nasimi: an Azerbaijani language layer over Python."""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import runpy
import sys
import tempfile
import tokenize
import traceback
from contextlib import redirect_stderr, redirect_stdout
from dataclasses import dataclass
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs


ROOT = Path(__file__).resolve().parent
LANGUAGE_DIR = ROOT / "languages"
SUPPORTED_LANGUAGES = ("azj", "azb")


class NasimiError(Exception):
    """User-facing Nasimi error."""


@dataclass
class TranslationData:
    words: dict[str, str]
    functions: dict[str, dict[str, str]]


def load_translation_data(lang_name: str) -> TranslationData:
    path = LANGUAGE_DIR / f"{lang_name}.json"
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as exc:
        raise NasimiError(
            f"'{lang_name}' dili tapılmadı. Seçimlər: {', '.join(SUPPORTED_LANGUAGES)}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise NasimiError(f"{path} faylında JSON xətası var: {exc}") from exc

    functions = data.pop("functions", {})
    return TranslationData(words=data, functions=functions)


def replace_phrases(code: str, functions: dict[str, dict[str, str]]) -> str:
    for func_data in functions.values():
        regex = func_data["regex"]
        replacement = func_data["replacement"]
        code = re.sub(regex, replacement, code, flags=re.MULTILINE)
    return code


class CodeTranslator:
    def __init__(self, lang_name: str, file_name: str | None = None):
        self.lang_name = lang_name
        self.file_name = file_name
        data = load_translation_data(lang_name)
        self.words = data.words
        self.functions = data.functions

    def translate_code(self, code: str) -> str:
        code = replace_phrases(code, self.functions)
        output_tokens = []
        stream = io.StringIO(code).readline

        try:
            tokens = tokenize.generate_tokens(stream)
            for token in tokens:
                token_type, token_text, start, end, line = token
                if token_type == tokenize.NAME:
                    token_text = self.words.get(token_text, token_text)
                output_tokens.append((token_type, token_text, start, end, line))
        except tokenize.TokenError as exc:
            raise NasimiError(f"Oxuma xətası: {exc}") from exc

        translated = tokenize.untokenize(output_tokens)
        return translated.replace("NASIMI_VARIABLE_PLACEHOLDER ", "")

    def translate_file(self) -> str:
        if not self.file_name:
            raise NasimiError("Fayl adı verilməyib.")
        path = Path(self.file_name)
        try:
            source_code = path.read_text(encoding="utf-8")
        except FileNotFoundError as exc:
            raise NasimiError(f"Fayl tapılmadı: {path}") from exc
        return self.translate_code(source_code)

    def run(self) -> int:
        translated_code = self.translate_file()
        source_path = Path(self.file_name or "input.nasimi")
        cache_file = source_path.parent / ".nasimi-cache" / f"{source_path.name}.py"
        cache_file.parent.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(translated_code, encoding="utf-8")
        return run_python(cache_file)


def run_python(path: Path) -> int:
    old_argv = sys.argv[:]
    old_path = sys.path[:]
    sys.argv = [str(path)]
    sys.path.insert(0, str(path.parent.resolve()))
    try:
        runpy.run_path(str(path), run_name="__main__")
        return 0
    except SystemExit as exc:
        return int(exc.code or 0) if isinstance(exc.code, int) else 1
    except Exception:
        traceback.print_exc()
        return 1
    finally:
        sys.argv = old_argv
        sys.path[:] = old_path


def run_source(lang: str, code: str) -> tuple[int, str, str, str]:
    translator = CodeTranslator(lang)
    stdout = io.StringIO()
    stderr = io.StringIO()
    try:
        translated = translator.translate_code(code)
    except NasimiError as exc:
        return 1, "", str(exc), ""

    with tempfile.TemporaryDirectory(prefix="nasimi-") as temp_dir:
        path = Path(temp_dir) / "playground.py"
        path.write_text(translated, encoding="utf-8")
        with redirect_stdout(stdout), redirect_stderr(stderr):
            status = run_python(path)
    return status, stdout.getvalue(), stderr.getvalue(), translated


class PlaygroundHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_POST(self) -> None:
        if self.path != "/run":
            self.send_error(404)
            return

        length = int(self.headers.get("content-length", "0"))
        payload = self.rfile.read(length).decode("utf-8")
        form = parse_qs(payload)
        lang = form.get("lang", ["azj"])[0]
        code = form.get("code", [""])[0]
        status, stdout, stderr, translated = run_source(lang, code)
        self.send_response(200)
        self.send_header("content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(
            json.dumps(
                {
                    "status": status,
                    "stdout": stdout,
                    "stderr": stderr,
                    "translated": translated,
                },
                ensure_ascii=False,
            ).encode("utf-8")
        )

    def end_headers(self) -> None:
        self.send_header("access-control-allow-origin", "*")
        super().end_headers()


def serve_playground(host: str, port: int) -> int:
    server = ThreadingHTTPServer((host, port), PlaygroundHandler)
    url_host = "localhost" if host in {"", "0.0.0.0"} else host
    print(f"Nasimi playground: http://{url_host}:{port}/playground.html")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDayandırıldı.")
    finally:
        server.server_close()
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="nasimi",
        description="Azerbaijani language layer over Python.",
    )
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Run a .nasimi file.")
    run_parser.add_argument("lang", choices=SUPPORTED_LANGUAGES)
    run_parser.add_argument("file")

    translate_parser = subparsers.add_parser(
        "translate", help="Print translated Python code."
    )
    translate_parser.add_argument("lang", choices=SUPPORTED_LANGUAGES)
    translate_parser.add_argument("file")

    serve_parser = subparsers.add_parser(
        "serve", help="Serve playground.html with a local run API."
    )
    serve_parser.add_argument("--host", default="127.0.0.1")
    serve_parser.add_argument(
        "--port", default=int(os.environ.get("NASIMI_PORT", 8008)), type=int
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) == 2 and argv[0] in SUPPORTED_LANGUAGES:
        argv = ["run", *argv]

    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "run":
        return CodeTranslator(args.lang, args.file).run()
    if args.command == "translate":
        print(CodeTranslator(args.lang, args.file).translate_file())
        return 0
    if args.command == "serve":
        return serve_playground(args.host, args.port)

    parser.print_help()
    return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except NasimiError as exc:
        print(f"Nasimi xətası: {exc}", file=sys.stderr)
        raise SystemExit(1)
