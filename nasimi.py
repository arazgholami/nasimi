import sys
import re
import os

class AzerbaijaniCodeRunner:
	az_to_en = {
		"başla": "def",
		"işləmə": "def",
		"başla:": ":",
		"qaytar": "return",
		"aralıq": "range",
		"özü": "self",
		"və": "and",
		"ya": "or",
		"dəyil": "not",
		"əgər": "if",
		"əgər:": ":",
		"əkshalda:": "else:",
		"əkshalda": "else",
		"üçün": "for",
		"üçün:": ":",
		"davamet": "continue",
		"dayan": "break",
		"denə": "try",
		"denə:": ":",
		"istisna": "except",
		"istisna:": ":",
		"nəhayət": "finally",
		"nəhayət:": ":",
		"girdir": "import",
		"sınıf": "class",
		"sınıf:": ":",
		"dəyişən": "AZJ_VARIABLE_PLACEHOLDER",
		"sabit": "const",
		"yoxsa": "elif",
		"yoxsa:": ":",
		"qədər": "while",
		"qədər:": ":",
		"ilə": "with",
		"ilə:": ":",
		"davamet": "pass",
		"növbəti": "next",
		"yarat": "def",
		"yarat:": ":",
		"çağır": "yield",
		"ləğvet": "raise",
		"hamısı": "all",
		"hərbiri": "any",
		"sil": "del",
		"özündədir": "in",
		"işlət": "exec",
		"hərtərəfli": "global",
		"lügət": "dict",
		"dəstə": "set",
		"siyahı": "list",
		"tərsinə": "reversed",
		"sadala": "enumerate",
		"uzunluq": "len",
		"dəyər": "value",
		"yaz": "print",
		"tip": "type",
		"İstisna": "Exception",
		"olaraq": "as",
		"doğru": 'True',
		"yanlış": 'False',
	}
	def __init__(self, file_name):
		self.file_name = file_name

	def translate_code(self, code):
		def replace(match):
			word = match.group(0)
			if word.startswith('"') and word.endswith('"'):
				return word
			if word.startswith('\'') and word.endswith('\''):
				return word
			translated_word = self.az_to_en.get(word, word)

			return translated_word

		translated_code = re.sub(r'\b\w+\b|".*?"', replace, code)

		return translated_code



	def run(self):
		with open(self.file_name, 'r', encoding='utf-8') as file:
			azerbaijani_code = file.read()

		translated_code = self.translate_code(azerbaijani_code)
		translated_code = translated_code.replace('AZJ_VARIABLE_PLACEHOLDER ', '')

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
	if len(sys.argv) != 2:
		print("Usage: python3 nasimi.py <filename.nasimi>")
		sys.exit(1)

	file_name = sys.argv[1]
	runner = AzerbaijaniCodeRunner(file_name)
	runner.run()
