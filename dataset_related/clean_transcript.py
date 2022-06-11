import os
import sys

sys.path.append('../')
import utility_module

def preprocess_dataset_folder(folder, language='te'):
	partitions = ['train', 'dev', 'test']
	print(f"==============Running validation for {folder}==============")
	for partition in partitions:
		print(f"==============Running validation for {folder}/{partition}==============")
		partition_folder = os.path.join(folder, f'{partition}')
		text_file = os.path.join(partition_folder, f'text')
		preprocess_transcript_file_text(text_file, language)

def clean_word(word, lang='te'):
	if(lang=='te'):
		new_word = utility_module.punctuation_and_others_remove(word)
		if(not utility_module.check_if_legal_lang_word(new_word, lang)):
			print(f"Illegal word: {word}")
			raise Exception(f"Illegal word: {word} -> new word: {new_word}")
		return new_word
			# return True
	else:
		raise Exception(f"Language {lang} not supported")



def preprocess_transcript_file_text(file, lang='te'):
	total_word_count = 0
	illegal_word_count = 0
	processed_word_count = 0
	full_lines = []
	with open(file, 'r') as f:
		lines = f.readlines()
		line_num=1
		for line in lines:
			line_split = line.split()
			if(len(line_split)==0):
				line_num+=1
				continue

			new_word_list = []

			for word in line_split[1:]:
				total_word_count+=1
				if(not utility_module.check_if_legal_lang_word(word, lang)):
					illegal_word_count+=1

					processed_word = clean_word(word, lang)
					if(utility_module.check_if_legal_lang_word(processed_word, lang)):
						processed_word_count+=1
						# print(f"In line number {line_num} : {line}\t{word}\t{repr(word).encode('utf-8')}")
						new_word_list.append(processed_word)
					else:
						raise Exception(f"Illegal word: {word} -> new word: {processed_word}")
				else:
					new_word_list.append(word)
				
			processed_line = " ".join(new_word_list)
			full_line = f"{line_split[0]}\t{processed_line}"
			full_lines.append(full_line)
	
	# Get parent folder of file
	foldername= os.path.dirname(file)
	new_file_name = f"{foldername}/processed_text"

	with open(new_file_name, 'w') as f:
		for i in range(len(full_lines)):
			if(i!=len(full_lines)-1):
				f.write(full_lines[i]+'\n')
			else:
				f.write(full_lines[i])
	
	print(f"File {file} Total line count:{line_num-1} word count: {total_word_count}, illegal word count: {illegal_word_count} processed_word_count: {processed_word_count}")





if(__name__ == "__main__"):
	# count_illegal_words_folder('tamil_db_files/dataset_files/commonvoice_tamil/transcription', language='ta')
	# count_illegal_words_folder('tamil_db_files/dataset_files/iitm_asr_tamil/transcription', language='ta')
	# count_illegal_words_folder('tamil_db_files/dataset_files/openslr_tamil/transcription', language='ta')
	# count_illegal_words_folder('tamil_db_files/dataset_files/microsoft_tamil/transcription', language='ta')

	preprocess_dataset_folder('telugu_db_files/dataset_files/microsoft_telugu/transcription', language='te')
	preprocess_dataset_folder('telugu_db_files/dataset_files/openslr_telugu/transcription', language='te')


