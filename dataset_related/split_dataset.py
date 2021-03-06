import os
import sys
import random



def create_dev_test_train_from_full(text_file_name):
    #Get parent directory of text_file_name
    parent_dir = os.path.dirname(text_file_name)

    dev_set_fraction = 0.1
    test_set_fraction = 0.1
    


    with open(text_file_name, "r") as f:
        lines = [line.rstrip() for line in f]
        random.shuffle(lines)
        total_num_lines = len(lines)
        dev_num_lines = int(total_num_lines * dev_set_fraction)
        test_num_lines = int(total_num_lines * test_set_fraction)

        dev_lines = [line.split("\t") for line in lines[:dev_num_lines]]
        dev_lines = sorted(dev_lines, key=lambda x: x[0])
        test_lines = [line.split("\t") for line in lines[dev_num_lines:dev_num_lines+test_num_lines]]
        test_lines = sorted(test_lines, key=lambda x: x[0])
        new_train_lines = [line.split("\t") for line in lines[dev_num_lines+test_num_lines:]]
        new_train_lines = sorted(new_train_lines, key=lambda x: x[0])

        with open(os.path.join(parent_dir,"dev_transcription.txt"), 'w') as file:
            file.write('\n'.join(["\t".join(line) for line in dev_lines]))

        with open(os.path.join(parent_dir,"test_transcription.txt"), 'w') as file:
            # file.write('\n'.join(test_lines))
            file.write('\n'.join(["\t".join(line) for line in test_lines]))

        with open(os.path.join(parent_dir,"train_transcription.txt"), 'w') as file:
            # file.write('\n'.join(new_train_lines))
            file.write('\n'.join(["\t".join(line) for line in new_train_lines]))

#For microsoft speech corpus
def create_dev_partition_from_train(text_file_name):
    #Get parent directory of text_file_name
    parent_dir = os.path.dirname(text_file_name)
    
    dev_set_fraction = 0.1


    with open(text_file_name, "r") as f:
        lines = [line.rstrip() for line in f]
        random.shuffle(lines)
        total_num_lines = len(lines)
        dev_num_lines = int(total_num_lines * dev_set_fraction)

        dev_lines = lines[:dev_num_lines]
        new_train_lines = lines[dev_num_lines:]

        with open(os.path.join(parent_dir,"dev_transcription.txt"), 'w') as file:
            file.write('\n'.join(dev_lines))

        with open(os.path.join(parent_dir,"new_train_transcription.txt"), 'w') as file:
            file.write('\n'.join(new_train_lines))

if(len(sys.argv)>1):
    create_dev_partition_from_train(sys.argv[1])
else:
    # microsoft_tamil_train_file = "./tamil_db_files/dataset_files/microsoft_tamil/train_transcription.txt"
    microsoft_telugu_train_file = "./telugu_db_files/dataset_files/microsoft_telugu/train_transcription.txt"
    # openslr_tamil_text_transcript_file="./tamil_db_files/dataset_files/openslr_tamil/combined.tsv"
    openslr_telugu_text_transcript_file="./telugu_db_files/dataset_files/openslr_telugu/combined.tsv"
    # create_dev_partition_from_train(microsoft_tamil_train_file)
    # create_dev_partition_from_train(microsoft_telugu_train_file)
    create_dev_test_train_from_full(openslr_telugu_text_transcript_file)
    # create_dev_test_train_from_full(openslr_text_transcript_file)

