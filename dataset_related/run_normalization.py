from black import main
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
import os

def normalize_transcription_folder(folder, language='te'):
	partitions = ['train', 'dev', 'test']
	print(f"==============Running normalization for {folder}==============")
	for partition in partitions:
		partition_folder = os.path.join(folder, f'{partition}')
		text_file = os.path.join(partition_folder, f'text')
		normalize_text_file(text_file, language)

def normalize_text_file(file, language='te'):
	remove_nuktas=True
	factory=IndicNormalizerFactory()
	normalizer=factory.get_normalizer(language,remove_nuktas=remove_nuktas)

	total_word_count = 0
	normalized_count = 0
	with open(file, 'r') as f:
		lines = f.readlines()
		line_num=1
		for line in lines:
			if(len(line.split())==0):
				line_num+=1
				continue

			for word in line.split()[1:]:
				total_word_count+=1
				normalized_word = normalizer.normalize(word)
				if(normalized_word != word):
					print(f"In line number {line_num} : {line}\t{word} -> {normalized_word}\n\t{repr(word).encode('utf-8')} -> {repr(normalized_word).encode('utf-8')}")
					normalized_count+=1
			
			line_num+=1
	
	print(f"File {file} Total line count:{line_num-1} word count: {total_word_count}, normalized count: {normalized_count}")


if(__name__ == "__main__"):
	# normalize_text_file('telugu_db_files/dataset_files/microsoft_telugu/train_transcription.txt')
	# normalize_text_file('tamil_db_files/dataset_files/commonvoice_tamil/train_transcription.txt', language='ta')
	# normalize_transcription_folder('tamil_db_files/dataset_files/commonvoice_tamil/transcription', language='ta')
	# normalize_transcription_folder('tamil_db_files/dataset_files/iitm_asr_tamil/transcription', language='ta')
	# normalize_transcription_folder('tamil_db_files/dataset_files/openslr_tamil/transcription', language='ta')
	# normalize_transcription_folder('tamil_db_files/dataset_files/microsoft_tamil/transcription', language='ta')
	normalize_transcription_folder('telugu_db_files/dataset_files/microsoft_telugu/transcription', language='te')
	normalize_transcription_folder('telugu_db_files/dataset_files/openslr_telugu/transcription', language='te')