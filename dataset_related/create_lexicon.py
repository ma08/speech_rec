import os
import sys
import random

from pathlib import Path

import re
import helper


from tamil import utf8

def get_lexicon(folder_path):
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
                    if(not helper.check_if_tamil_word(word)):
                        # print(f"{word} is not a tamil word")
                        non_tamil_count +=1
                    else:
                        tamil_word_set.add(word)
    
    with open(f"{folder_path}/lexicon", 'w') as file:
        for tamil_word in tamil_word_set:
            letters = utf8.get_letters(tamil_word)
            file.write(f"{tamil_word}\t{' '.join(letters)}\n")


    print(f"Total words: {total_count}, non tamil count {non_tamil_count} set count: {len(tamil_word_set)}")

            # print(lines)

if(len(sys.argv)>1):
    pass
else:
    #create_formatted_files_mozillacv(mozillacv_tamil_path)
    # remove_punctuation_mozillacv(mozillacv_tamil_path)
    # fix_asriitm_wavscp_path("~/kaldi/egs/tamil_telugu_proj/s5_r3/db/asriitm_tamil")
    # fix_asriitm_wavscp_path("dataset_files/iitm_asr_tamil")

    kaldi_db = "kaldi_db/combined_transcription/"
    get_lexicon(kaldi_db)
    #remove_punctuation_combined(kaldi_db)


