import os
import sys
import random

from pathlib import Path

from toml import TomlArraySeparatorEncoder
mozillacv_tamil_path = "./dataset_files/commonvoice_tamil"
def create_formatted_files_mozillacv(folder_path):
    clientid_set = set()

    for partition in "train", "dev", "test":
        file_name = os.path.join(folder_path, f"{partition}.tsv")
        with open(file_name, "r") as f:
            lines = [line.rstrip().split('\t') for line in f][1:]
            clientid_set.update([line[0] for line in lines])
    
    client_count = 0
    speaker_id_dic = {}

    client_dic_lines = []
    for clientid in  clientid_set:
        # print("{:02d}".format(number))
        client_count_str = "{:03d}".format(client_count)
        speaker_id_dic[clientid] = f"mcvspeaker{client_count_str}"
        client_dic_lines.append(f"{clientid}\t{speaker_id_dic[clientid]}")
        client_count += 1

    with open(os.path.join(folder_path,f"speakerid.tsv"), 'w') as file:
        file.write('\n'.join(client_dic_lines))


    
    for partition in "train", "dev", "test":
        file_name = os.path.join(folder_path, f"{partition}.tsv")
        print(partition)
        """
        ['client_id', 'path', 'sentence', 'up_votes', 'down_votes', 'age', 'gender', 'accents', 'locale', 'segment']
        """
        with open(file_name, "r") as f:
            lines = [line.rstrip().split('\t') for line in f][1:]
            # file_path = lines[0][1]
            # sentence = lines[0][2]
            # filename_stem = Path(file_path).stem
            output_lines = [f"{speaker_id_dic[line[0]]}-{Path(line[1]).stem}\t{line[2]}" for line in lines]

            with open(os.path.join(folder_path,f"{partition}_transcription.txt"), 'w') as file:
                file.write('\n'.join(output_lines))
import string     
# Printing Inbuilt punctuation function
# print(string.punctuation)            

# Function for removing punctuation
def punctuation_remove(text_data): 
    # Appending non punctuated words
    punctuation ="".join([t for t in text_data if t not in string.punctuation])  
    return punctuation

def remove_punctuation_combined(folder_path):
    for partition in "train", "dev", "test":
        file_name = os.path.join(folder_path, f"{partition}/text")
        with open(file_name, "r") as f:
            lines = [line.rstrip().split() for line in f]
            processed_lines = [f"{line[0]}\t{punctuation_remove(' '.join(line[1:]))}" for line in lines]
            # processed_lines = [f"{punctuation_remove(line[1])}" for line in lines]
            with open(os.path.join(folder_path,f"{partition}/text"), 'w') as file:
                file.write('\n'.join(processed_lines))
 
def remove_punctuation_mozillacv(folder_path):
    for partition in "train", "dev", "test":
        file_name = os.path.join(folder_path, f"{partition}_transcription.txt")
        with open(file_name, "r") as f:
            lines = [line.rstrip().split('\t') for line in f]
            processed_lines = [f"{line[0]}\t{punctuation_remove(line[1])}" for line in lines]
            # processed_lines = [f"{punctuation_remove(line[1])}" for line in lines]
            with open(os.path.join(folder_path,f"{partition}_text_processed.txt"), 'w') as file:
                file.write('\n'.join(processed_lines))
            # for i in range(len(lines)):
                # print(f"\n----\n{lines[i][1]}\n{processed_lines[i]}\n----")
                # print(f"\n----\noriginal: {lines[i]}\nprocessed: {processed_lines[i]}\n----")

def fix_asriitm_wavscp_path(asriitm_folder_path):
    folder_path_input = asriitm_folder_path
    asriitm_folder_path = os.path.expanduser(asriitm_folder_path)
    folder_path = f"{asriitm_folder_path}/transcription"
    for partition in "train", "dev", "test":
        current_wavscp_file = os.path.join(folder_path, f"{partition}/wav.scp")
        file_name = os.path.join(folder_path, f"{partition}_text_processed.txt")
        with open(current_wavscp_file, "r") as f:
            delimiter = " "
            if(partition == "train"):
                split_lines = []
                for line in f:
                    if(len(line.split(" ")) == 2):
                        split_lines.append(line.split(" "))
                    else:
                        split_lines.append(line.split("\t"))
            else:
                split_lines = [line.rstrip().split(delimiter) for line in f]

            # for l in split_lines:
                # if(len(l)!=2):
                    # print(f"\n--{partition}--\n{l}\n----")
            # print(split_lines[0])
            processed_lines = [f"{sp_line[0]} {folder_path_input}/{sp_line[1]}" for sp_line in split_lines]
        with open(current_wavscp_file, 'w') as file:
            file.write('\n'.join(processed_lines))


import re
def check_if_tamil_word(word):
    r = re.compile(r'^[\u0B80-\u0BFF]+$')
    if(r.search(word)):
        return True
    else:
        return False

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
                    if(not check_if_tamil_word(word)):
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

