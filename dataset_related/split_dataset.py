import os
import sys
import random

microsoft_train_file = "./dataset_files/microsoft_tamil/train_transcription.txt"

#For microsoft speech corpus
def create_dev_partition_from_train(text_file_name):
    #Get parent directory of text_file_name
    parent_dir = os.path.dirname(text_file_name)
    


    with open(text_file_name, "r") as f:
        lines = [line.rstrip() for line in f]
        random.shuffle(lines)
        total_num_lines = len(lines)
        dev_num_lines = int(total_num_lines * 0.01)

        dev_lines = lines[:dev_num_lines]
        new_train_lines = lines[dev_num_lines:]

        with open(os.path.join(parent_dir,"dev_transcription.txt"), 'w') as file:
            file.write('\n'.join(dev_lines))

        with open(os.path.join(parent_dir,"new_train_transcription.txt"), 'w') as file:
            file.write('\n'.join(new_train_lines))
if(len(sys.argv)>1):
    create_dev_partition_from_train(sys.argv[1])
else:
    create_dev_partition_from_train(microsoft_train_file)


