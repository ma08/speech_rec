import sys

from pydantic import FilePath
sys.path.append('../')
import utility_module

def validate_line_space(line, words):
	return " ".join(words) == line

def validate_text(file_path):
	print(f"processing {file_path}")
	space_error = 0
	tamil_word_error = 0
	with open(file_path, 'r') as file:
		for line in file:
			words = line.split()
			if(not validate_line_space):
				space_error+=1
			for word in words:
				if(not utility_module.check_if_tamil_word(word)):
					print(f"culprit word {word}")
					tamil_word_error+=1
	print(f"file {file_path} space error {space_error} tamil word error {tamil_word_error}")

validate_text("preprocessing/stage5_out_rand25klines.txt")
validate_text("preprocessing/iitmasr_text.txt")
validate_text("preprocessing/iitmasr_text_processed.txt")

