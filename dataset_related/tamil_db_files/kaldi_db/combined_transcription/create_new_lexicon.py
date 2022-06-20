import os
import sys
import random

from pathlib import Path

import re

from black import main
sys.path.append('../../../../')
import utility_module

import print_timestamp_module
print = print_timestamp_module.timestamped_print

def create_new_tamil_lexicon(path):

	with open(path, "r") as f:
		with open(f"new_tamil.dic", 'w') as file:
			for line in f:
				line_split = line.split()
				if(len(line_split)>=1):
					letters = utility_module.split_word_to_letters(line_split[0], 'ta')
					file.write(f"{line_split[0]}\t{' '.join(letters)}\n")

if __name__ == '__main__':
	create_new_tamil_lexicon("lexicon.txt")
	#open file at path