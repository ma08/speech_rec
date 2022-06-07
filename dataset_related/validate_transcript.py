import os

import sys
sys.path.append('../')
import utility_module

def count_illegal_words_folder(folder, language='te'):
	partitions = ['train', 'dev', 'test']
	print(f"==============Running validation for {folder}==============")
	for partition in partitions:
		print(f"==============Running validation for {folder}/{partition}==============")
		partition_folder = os.path.join(folder, f'{partition}')
		text_file = os.path.join(partition_folder, f'text')
		count_illegal_words(text_file, language)



def count_illegal_words(file, lang='te'):
	total_word_count = 0
	illegal_word_count = 0
	with open(file, 'r') as f:
		lines = f.readlines()
		line_num=1
		for line in lines:
			if(len(line.split())==0):
				line_num+=1
				continue

			for word in line.split()[1:]:
				total_word_count+=1
				if(not utility_module.check_if_legal_lang_word(word, lang)):
					illegal_word_count+=1
					print(f"In line number {line_num} : {line}\t{word}\t{repr(word).encode('utf-8')}")
			
			line_num+=1
	
	print(f"File {file} Total line count:{line_num-1} word count: {total_word_count}, illegal word count: {illegal_word_count}")


if(__name__ == "__main__"):
	# count_illegal_words_folder('tamil_db_files/dataset_files/commonvoice_tamil/transcription', language='ta')
	# count_illegal_words_folder('tamil_db_files/dataset_files/iitm_asr_tamil/transcription', language='ta')
	# count_illegal_words_folder('tamil_db_files/dataset_files/openslr_tamil/transcription', language='ta')
	# count_illegal_words_folder('tamil_db_files/dataset_files/microsoft_tamil/transcription', language='ta')

	count_illegal_words_folder('telugu_db_files/dataset_files/microsoft_telugu/transcription', language='te')
	count_illegal_words_folder('telugu_db_files/dataset_files/openslr_telugu/transcription', language='te')


