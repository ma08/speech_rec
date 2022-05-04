import os
import sys
import random

from pathlib import Path
mozillacv_tamil_path = "./dataset_files/commonvoice_tamil"
def create_formatted_files_mozillacv(folder_path):
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
            output_lines = [f"{Path(line[1]).stem}\t{line[2]}" for line in lines]

            with open(os.path.join(folder_path,f"{partition}_transcription.txt"), 'w') as file:
                file.write('\n'.join(output_lines))
import string     
# Printing Inbuilt punctuation function
print(string.punctuation)            

# Function for removing punctuation
#https://www.geeksforgeeks.org/python-preprocessing-of-tamil-text/
def punctuation_remove(text_data): 
    # Appending non punctuated words
    punctuation ="".join([t for t in text_data if t not in string.punctuation])  
    return punctuation

def remove_punctuation_mozillacv(folder_path):
    for partition in "train", "dev", "test":
        file_name = os.path.join(folder_path, f"{partition}_transcription.txt")
        with open(file_name, "r") as f:
            lines = [line.rstrip().split('\t') for line in f]
            processed_lines = [f"{line[0]} {punctuation_remove(line[1])}" for line in lines]
            # processed_lines = [f"{punctuation_remove(line[1])}" for line in lines]
            with open(os.path.join(folder_path,f"{partition}_text_processed.txt"), 'w') as file:
                file.write('\n'.join(processed_lines))
            # for i in range(len(lines)):
                # print(f"\n----\n{lines[i][1]}\n{processed_lines[i]}\n----")
                # print(f"\n----\noriginal: {lines[i]}\nprocessed: {processed_lines[i]}\n----")






if(len(sys.argv)>1):
    pass
else:
    # create_formatted_files_mozillacv(mozillacv_tamil_path)
    remove_punctuation_mozillacv(mozillacv_tamil_path)

