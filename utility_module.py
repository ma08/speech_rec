import os
import sys
import random

sys.path.append('../')
import print_timestamp_module
print = print_timestamp_module.timestamped_print

from pathlib import Path

import string     
import re

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

def contains_multiple_spaces(s):
    return bool(re.search(r' {2,}', s))

"""
https://stackoverflow.com/a/2077906/3465519
"""
def fix_multiple_whitespace(input_text, isunicode_whitespace=True):
    text = input_text
    if(isunicode_whitespace):
        _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
        text = _RE_COMBINE_WHITESPACE.sub(" ", text).strip()
        return text
    else:
        _RE_COMBINE_WHITESPACE = re.compile(r"(?a:\s+)")
        _RE_STRIP_WHITESPACE = re.compile(r"(?a:^\s+|\s+$)")
        text = _RE_COMBINE_WHITESPACE.sub(" ", text)
        text = _RE_STRIP_WHITESPACE.sub("", text)
        return text


# Printing Inbuilt punctuation function
# print(string.punctuation)            

# Function for removing punctuation
def punctuation_and_others_remove(text_data): 
    # Appending non punctuated words
    '“”‘’‚◯·—–'
    char_list = [
        '“', #U+201C : LEFT DOUBLE QUOTATION MARK {double turned comma quotation mark}
        "”", #U+201D : RIGHT DOUBLE QUOTATION MARK {double comma quotation mark}
        '‘', #U+2018 : LEFT SINGLE QUOTATION MARK {single turned comma quotation mark}
        '’', #U+2019 : RIGHT SINGLE QUOTATION MARK {single comma quotation mark}
        '‚', #U+201A : SINGLE LOW-9 QUOTATION MARK {low single comma quotation mark}
        '◯', #U+25EF : LARGE CIRCLE
        '·', #U+00B7 : MIDDLE DOT {midpoint (in typography); Georgian comma; Greek middle dot (ano teleia)}
        '—', #U+2014 : EM DASH {em dash}
        '–', #U+2013 : EN DASH,
        '•', #U+2022 : BULLET {black small circle},
        '…', #U+2026 : HORIZONTAL ELLIPSIS {three dot leader},
        '″', #U+2033 : DOUBLE PRIME {seconds, inches}
        '\u200c', #U+200c : ZERO WIDTH NON-JOINER {zero-width non-joiner}
        '\ufeff', #U+FEFF : ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP}
    ]
    punc_char_string = string.punctuation+"".join(char_list)
    punctuation ="".join([t for t in text_data if t not in punc_char_string])  
    return punctuation

tamil_r = re.compile(r'^[\u0B80-\u0BFF]+$')
def check_if_tamil_word(word):
    if(tamil_r.search(word)):
        return True
    else:
        return False

#https://unicode.org/charts/PDF/U0C00.pdf
telugu_r = re.compile(r'^[\u0C00-\u0C7F]+$')
def check_if_telugu_word(word):
    if(telugu_r.search(word)):
        return True
    else:
        return False

re_dic = {
    'te': telugu_r,
    'ta': tamil_r,
}


def check_if_legal_lang_word(word, lang='te'):
    lang_r = re_dic[lang]
    if(lang_r.search(word)):
        return True
    else:
        return False



'''
உருவாக்கப்பட்டதுஇதுExpressinho
Cookஅடுத்து
even empty tam/eng subparts are considered to pass
'''
def check_tameng_or_engtam(word):
    w_len = len(word)
    for i in range(w_len):
        pref = word[:i]
        suf = word[i:]
        if((check_if_tamil_word(pref) and suf.isalnum()) or (pref.isalnum() and check_if_tamil_word(suf))):
            return True, i

    return False, -1


"""
உருவாக்கப்பட்டதுஇதுExpressinho
Cookஅடுத்து
"""
def split_engtam_or_tameng_word(word):
    is_tameng, split_index = check_tameng_or_engtam(word)
    if(is_tameng):
        return True, f"{word[:split_index]} {word[split_index:]}"
    else:
        return False,word


def remove_punctuation_combined(folder_path):
    for partition in "train", "dev", "test":
        file_name = os.path.join(folder_path, f"{partition}/text")
        with open(file_name, "r") as f:
            lines = [line.rstrip().split() for line in f]
            processed_lines = [f"{line[0]}\t{punctuation_and_others_remove(' '.join(line[1:]))}" for line in lines]
            # processed_lines = [f"{punctuation_remove(line[1])}" for line in lines]
            with open(os.path.join(folder_path,f"{partition}/text"), 'w') as file:
                file.write('\n'.join(processed_lines))
 
def remove_punctuation_mozillacv(folder_path):
    for partition in "train", "dev", "test":
        file_name = os.path.join(folder_path, f"{partition}_transcription.txt")
        with open(file_name, "r") as f:
            lines = [line.rstrip().split('\t') for line in f]
            processed_lines = [f"{line[0]}\t{punctuation_and_others_remove(line[1])}" for line in lines]
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












if(len(sys.argv)>1):
    pass
else:
    #create_formatted_files_mozillacv(mozillacv_tamil_path)
    # remove_punctuation_mozillacv(mozillacv_tamil_path)
    # fix_asriitm_wavscp_path("~/kaldi/egs/tamil_telugu_proj/s5_r3/db/asriitm_tamil")
    # fix_asriitm_wavscp_path("dataset_files/iitm_asr_tamil")
    #remove_punctuation_combined(kaldi_db)
    pass

