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
            output_lines = [f"{Path(line[1]).stem} {line[2]}" for line in lines]

            with open(os.path.join(folder_path,f"{partition}_transcription.txt"), 'w') as file:
                file.write('\n'.join(output_lines))




if(len(sys.argv)>1):
    pass
else:
    create_formatted_files_mozillacv(mozillacv_tamil_path)

