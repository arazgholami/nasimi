import sys
import re

class AzerbaijaniCodeRunner:
	az_to_en = {
		"başla": "def",
		"işləmə": "def",
		"başla:": ":",
		"qaytar": "return",
		"araliq": "range",
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
		"davam-et": "continue",
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
		"davam-et": "pass",
		"növbəti": "next",
		"yarat": "def",
		"yarat:": ":",
		"çağır": "yield",
		"ləğvet": "raise",
		"hamısı": "all",
		"hər-biri": "any",
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
		'İstisna': "Exception",
		"olaraq": "as"
	}

	def __init__(self, file_name):
		self.file_name = file_name

	def translate_code(self, code):
		def replace(match):
			word = match.group(0)
			if word.startswith('"') and word.endswith('"'):
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

		print(translated_code)

		try:
			exec(translated_code, globals())
		except Exception as e:
			print("Error occurred while executing the translated code:", e)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 nasimi.py <filename.nasimi>")
		sys.exit(1)

	file_name = sys.argv[1]
	runner = AzerbaijaniCodeRunner(file_name)
	runner.run()
