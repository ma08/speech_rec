import os
import sys
import random

from pathlib import Path

import re
sys.path.append('../')
import utility_module

import print_timestamp_module
print = print_timestamp_module.timestamped_print

from tamil import utf8

"""
similar to phonemes
"""
def split_word_to_letters(tamil_word):
	return utf8.get_letters(tamil_word)

def get_lexicon_tamil(folder_path):
    folder_path_orig  = folder_path
    folder_path = os.path.expanduser(folder_path)
    tamil_word_set = set()
    total_count = 0
    non_tamil_count = 0
    for partition in "train", "dev", "test":
        cur_folder_path = f"{folder_path}/{partition}"
        cur_text_file = f"{cur_folder_path}/text"
        with open(cur_text_file, "r") as f:
            lines = [line.split()[1:] for line in f]
            for line in lines:
                for word in line:
                    total_count+=1
                    if(not utility_module.check_if_tamil_word(word)):
                        # print(f"{word} is not a tamil word")
                        non_tamil_count +=1
                    else:
                        tamil_word_set.add(word)
    
    with open(f"{folder_path}/tamil.dic", 'w') as file:
        for tamil_word in tamil_word_set:
            letters = split_word_to_letters(tamil_word)
            file.write(f"{tamil_word}\t{' '.join(letters)}\n")


    print(f"Total words: {total_count}, non tamil count {non_tamil_count} set count: {len(tamil_word_set)}")

            # print(lines)

def get_lexicon_telugu(folder_path):
    folder_path_orig  = folder_path
    folder_path = os.path.expanduser(folder_path)
    telugu_word_set = set()
    total_count = 0
    non_telugu_count = 0
    for partition in "train", "dev", "test":
        cur_folder_path = f"{folder_path}/{partition}"
        cur_text_file = f"{cur_folder_path}/text"
        with open(cur_text_file, "r") as f:
            lines = [line.split()[1:] for line in f]
            for line in lines:
                for word in line:
                    total_count+=1
                    if(not utility_module.check_if_telugu_word(word)):
                        # print(f"{word} is not a tamil word")
                        non_telugu_count +=1
                    else:
                        telugu_word_set.add(word)
    
    with open(f"{folder_path}/telugu.dic", 'w') as file:
        for telugu_word in telugu_word_set:
            letters = utility_module.split_word_to_letters(telugu_word, 'te')
            file.write(f"{telugu_word}\t{' '.join(letters)}\n")


    print(f"Total words: {total_count}, non tamil count {non_telugu_count} set count: {len(telugu_word_set)}")

            # print(lines)


if(len(sys.argv)>1):
    pass
else:
    #create_formatted_files_mozillacv(mozillacv_tamil_path)
    # remove_punctuation_mozillacv(mozillacv_tamil_path)
    # fix_asriitm_wavscp_path("~/kaldi/egs/tamil_telugu_proj/s5_r3/db/asriitm_tamil")
    # fix_asriitm_wavscp_path("dataset_files/iitm_asr_tamil")

    # kaldi_db = "~/kaldi/egs/tamil_telugu_proj/s5_r3/db/combined_transcription"
    # get_lexicon_tamil(kaldi_db)

    kaldi_db_telugu = "~/kaldi/egs/tamil_telugu_proj/s5_r3/db/telugu_combined_transcription"
    get_lexicon_telugu(kaldi_db_telugu)
	# print(f"print(split_word_to_letters('நட‌க்க')): {split_word_to_letters('நட‌க்க')}")
	# print(f"print(split_word_to_letters('அதிகாரி﻿')): {split_word_to_letters('அதிகாரி﻿')}")
	# print(split_word_to_letters("நட‌க்க"))
    #remove_punctuation_combined(kaldi_db)


