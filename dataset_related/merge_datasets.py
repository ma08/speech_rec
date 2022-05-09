import sys
sys.path.append('../')
import print_timestamp_module
print = print_timestamp_module.timestamped_print
import os
import sox
#https://github.com/rabitt/pysox
import sys
from pathlib import Path
import shutil

file_names = ['spk2utt', 'segments', 'utt2dur', 'text', 'utt2spk', 'wav.scp']

def merge_datasets(folder_path):
    folder_path_input = folder_path
    folder_path = os.path.expanduser(folder_path)
    target_folder = f"{folder_path}/combined_transcription"
    for partition in "train", "dev", "test":
        subtarget_folder = f"{target_folder}/{partition}"
        Path(subtarget_folder).mkdir(parents=True, exist_ok=True)
        for i in range(len(file_names)):
            file_name = file_names[i]
            target_file = f"{subtarget_folder}/{file_name}"
            with open(target_file, 'wb') as wfd:
                for dataset in "asriitm_tamil", "mozillacv_tamil", "microsoft_tamil", "openslr_tamil":
                    print(f"Running on {dataset} {partition} {file_name}")
                    current_input_file = f"{folder_path}/{dataset}/transcription/{partition}/{file_name}"
                    with open(current_input_file,'rb') as fd:
                        shutil.copyfileobj(fd, wfd)
                        fd.seek(-len(os.linesep), 2)
                        if fd.read() != os.linesep and i != len(file_names)-1:
                            wfd.write(os.linesep)


if(len(sys.argv)>1):
    merge_datasets(sys.argv[1])
else:
    db_path = "~/kaldi/egs/tamil_telugu_proj/s5_r3/db"
    merge_datasets(db_path)
    # microsoft_dataset_name = "microsoft"
    print("finished")




