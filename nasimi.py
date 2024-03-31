import sys
import re
import os
import json

def load_translation_data(lang_name):
    try:
        with open(f'./languages/{lang_name}.json', 'r') as f:
            data = json.load(f)
            translation_dict = data
            functions = data.get('functions', {})
        return translation_dict, functions
    except FileNotFoundError:
        print(f"Error: Translation data for '{lang_name}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{lang_name}.json'.")
        sys.exit(1)

def replace_functions(code, functions):
    if functions:
        for func_name, func_data in functions.items():
            regex = func_data['regex']
            replacement = func_data['replacement']
            code = re.sub(regex, replacement, code)
    return code

class CodeTranslator:
    def __init__(self, lang_name, file_name):
        self.file_name = file_name
        self.translation_dict, self.functions = load_translation_data(lang_name)

    def translate_code(self, code):
        def replace(match):
            word = match.group(0)
            if word.startswith('"') and word.endswith('"'):
                return word
            if word.startswith('\'') and word.endswith('\''):
                return word
            translated_word = self.translation_dict.get(word, word)
            return translated_word

        translated_code = replace_functions(code, self.functions)
        translated_code = re.sub(r'\b\w+\b|".*?"', replace, translated_code)
        return translated_code

    def run(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            source_code = file.read()
        translated_code = self.translate_code(source_code)
        translated_code = translated_code.replace('NASIMI_VARIABLE_PLACEHOLDER ', '')
        # print(translated_code)
        dir_name = os.path.dirname(self.file_name)
        filename = os.path.basename(self.file_name)
        cache_file_name = os.path.join(dir_name, '.cache', filename + '.py')
        os.makedirs(os.path.dirname(cache_file_name), exist_ok=True)
        with open(cache_file_name, 'w', encoding='utf-8') as cache_file:
            cache_file.write(translated_code)
        try:
            exec(compile(open(cache_file_name, 'rb').read(), cache_file_name, 'exec'), globals())
        except Exception as e:
            print("Error occurred while executing the translated code:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 nasimi.py <lang_name> <filename.nasimi>")
        sys.exit(1)
    lang_name = sys.argv[1]
    file_name = sys.argv[2]
    translator = CodeTranslator(lang_name, file_name)
    translator.run()