import sys
sys.path.append('../')
import print_timestamp_module
print = print_timestamp_module.print_timestamp
import os
import sox
#https://github.com/rabitt/pysox
import sys
from pathlib import Path
import shutil

sample_folder = "/home/sourya4/pro/columbia/spring22/fund_sp_rec/datasets/microsoftspeechcorpusindianlanguages/te-in-Train/Audios/"
home_path =  os.path.expanduser("~") 

def get_utt2spk_lines(fstems, dataset_name):
    if(dataset_name == "mozilla"):
        utt2spk_lines = [f"{fstem} {fstem.split('-')[0]}" for fstem in fstems]
    elif(dataset_name == "microsoft"):
        utt2spk_lines = [f"{fstem} {fstem}" for fstem in fstems]
    elif(dataset_name == "openslr"):
        utt2spk_lines = [f"{fstem} {fstem.split('_')[0]}_{fstem.split('_')[1]}" for fstem in fstems]
    
    return utt2spk_lines

def get_fstem_dur_secs(fstems, dataset_name, audio_folder):
    if(dataset_name == "mozilla"):
        fstem_dur_secs = [[fstem, sox.file_info.duration(f"{audio_folder}/{fstem.split('-')[1]}.wav")] for fstem in fstems]
    else:
        fstem_dur_secs = [[fstem, sox.file_info.duration(f"{audio_folder}/{fstem}.wav")] for fstem in fstems]
    
    return fstem_dur_secs

def get_wavscp_lines(fstems, dataset_name, audio_rel_folder):
    if(dataset_name == "mozilla"):
        wavscp_lines  = [f"{fstem} {audio_rel_folder}/{fstem.split('-')[1]}.wav" for fstem in fstems]
    else:
        wavscp_lines  = [f"{fstem} {audio_rel_folder}/{fstem}.wav" for fstem in fstems]
    
    return wavscp_lines






"""
This is to create data files for the input folder when there are no splits needed for the audio files
"""
def create_files(folder_path, dataset_name):
    folder_path_input = folder_path
    folder_path = os.path.expanduser(folder_path)
    # sample_path = "/home/sourya4/pro/columbia/spring22/fund_sp_rec/datasets/microsoftspeechcorpusindianlanguages/te-in-Train/Audios/000010013.wav"
    # folder_name = sample_folder
    #Iterate through all files in the folder that have .wav extension
    for partition in "train", "dev", "test":
        print(f"Running on {dataset_name} {partition}")
        counter_files = 0
        #Open and write to file line by line
        target_folder = f"{folder_path}/transcription/{partition}"
        Path(target_folder).mkdir(parents=True, exist_ok=True)
        transcript_file = f"{folder_path}/{partition}_transcription.txt"
        segment_file = f"{folder_path}/transcription/{partition}/segments"
        utt2spk_file = f"{folder_path}/transcription/{partition}/utt2spk"
        utt2dur_file = f"{folder_path}/transcription/{partition}/utt2dur"
        wav_scp_file = f"{folder_path}/transcription/{partition}/wav.scp"
        audio_folder = f"{folder_path}/Audio"
        audio_rel_folder = f"~/{os.path.relpath(audio_folder, home_path)}"

        with open(transcript_file, "r") as t_file:
            #Creating 'text' file by copying
            shutil.copyfile(transcript_file, f"{target_folder}/text")
            file_stems = [line.rstrip().split('\t')[0] for line in t_file]
            utt2spk_lines = get_utt2spk_lines(file_stems, dataset_name)
            fstem_dur_secs = get_fstem_dur_secs(file_stems, dataset_name, audio_folder)
            segment_lines = [f"{fstem_dur_sec[0]} {fstem_dur_sec[0]} 0.0 {fstem_dur_sec[1]}" for fstem_dur_sec in fstem_dur_secs]
            utt2dur_lines = [f"{fstem_dur_sec[0]} {fstem_dur_sec[1]}" for fstem_dur_sec in fstem_dur_secs]
            wavscp_lines  = get_wavscp_lines(file_stems, dataset_name, audio_rel_folder)

            with open(segment_file, 'w') as file:
                file.write('\n'.join(segment_lines))

            with open(wav_scp_file, 'w') as file:
                file.write('\n'.join(wavscp_lines))

            with open(utt2spk_file, 'w') as file:
                file.write('\n'.join(utt2spk_lines))

            with open(utt2dur_file, 'w') as file:
                file.write('\n'.join(utt2dur_lines))

if(len(sys.argv)>1):
    create_files(sys.argv[1])
else:
    # openslr_path = "~/kaldi/egs/tamil_telugu_proj/s5_r3/db/openslr_tamil"
    # openslr_dataset_name = "openslr"
    #create_files(openslr_path, openslr_dataset_name)
    mozilla_path = "~/kaldi/egs/tamil_telugu_proj/s5_r3/db/mozillacv_tamil"
    mozilla_dataset_name = "mozilla"
    create_files(mozilla_path, mozilla_dataset_name)
    print("finished")

