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
import utility_module

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


def process_tamil_transcript(file_path, dataset_name):
    print(f"Processing {file_path} for {dataset_name}")
    tamil_lines = []
    with open(file_path, "r") as t_file:
        pure_eng_lines_count = 0
        comb_word_lines_count = 0
        unclean_lines_count = 0
        # whitespace_fixed_lines_count = 0
        for input_line in t_file:
            culprit_words = []
            line = input_line.rstrip()
            is_clean = True
            is_comb_line = False
            audio_id_part = line.split()[0]
            transcript_text = " ".join(line.split()[1:])
            text_processed = utility_module.punctuation_and_others_remove(transcript_text)
            new_words = []
            has_pure_eng = False
            for word in text_processed.split():
                if(not utility_module.check_if_tamil_word(word)):
                    culprit_words.append(word)
                    # if(word.isalpha()):
                    if(word.isalnum()):
                        has_pure_eng = True
                        pure_eng_lines_count+=1
                        new_words.append(word)
                        is_clean = True
                        # is_clean = True
                        # print(f"!{transcript_text}! culprit:!{word}!")
                        # print(f"{word} is not tamil")
                        continue
                    # print("------------")
                    # print(f"!{line}! culprit:!{word}!")
                    # print(f"orig:!{transcript_text}! afterpunc:!{text_processed}!")
                    is_comb, processed_word = utility_module.split_engtam_or_tameng_word(word)
                    # print(f"is_comb: {is_comb} orig_wrod: !{word}! comb:!{processed_word}!")
                    if(is_comb):
                        comb_word_lines_count+=1
                        new_words.append(processed_word)
                        is_comb_line = True
                    else:
                        # unclean_lines_count+=1
                        is_clean = False
                        new_words.append(word)
                        continue
                else:
                    new_words.append(word)
            # final_line = line
            processed_text = ' '.join(new_words)
            final_line = f"{audio_id_part}\t{processed_text}"
            # whitespace_fixed_text = helper.fix_multiple_whitespace(processed_text,isunicode_whitespace=True)

            # if(whitespace_fixed_text != processed_text):
            #     whitespace_fixed_lines_count+=1


            if(is_clean):
                if(has_pure_eng or is_comb_line):


                    # print("!!!!!!!!!!!!!!!!!!!!")
                    # print(f"has_pure_eng {has_pure_eng} is_comb_line {is_comb_line}")
                    # print(f"{transcript_text}")
                    # print(f"{processed_line}")
                    # print("!!!!!!!!!!!!!!!!!!!!")
                    final_line = f"{audio_id_part}\t{processed_text}"
                # tamil_lines.append(final_line)
            else:
                unclean_lines_count+=1
                #sliding unclean so that <unk> can take care of it later
                print(f"not clean {transcript_text}")
                print(f"culprit words {culprit_words}")
                # print("------------")
                pass
            # print(f"{final_line}")
            tamil_lines.append(final_line)
    print(f"pure_eng_lines_count: {pure_eng_lines_count}")
    print(f"comb_word_lines_count: {comb_word_lines_count}")
    # print(f"whitespace_fixed_lines_count: {whitespace_fixed_lines_count}")
    print(f"unclean_lines_count: {unclean_lines_count}")
    return tamil_lines




def create_files_telugu(folder_path, dataset_name):
    folder_path_input = folder_path
    folder_path = os.path.expanduser(folder_path)

    for partition in "train", "dev", "test":
        print(f"Running on {dataset_name} {partition}")
        counter_files = 0
        #Open and write to file line by line
        target_folder = f"{folder_path}/transcription/{partition}"
        Path(target_folder).mkdir(parents=True, exist_ok=True)
        transcript_file = f"{folder_path}/transcription/{partition}/text"

        segment_file = f"{folder_path}/transcription/{partition}/segments"
        utt2spk_file = f"{folder_path}/transcription/{partition}/utt2spk"
        utt2dur_file = f"{folder_path}/transcription/{partition}/utt2dur"
        wav_scp_file = f"{folder_path}/transcription/{partition}/wav.scp"
        audio_folder = f"{folder_path}/Audio"
        audio_rel_folder = f"~/{os.path.relpath(audio_folder, home_path)}"

        #text file already cleaned and formatted for telugu

        with open(transcript_file, "r") as t_file:
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
        processed_text_lines = process_tamil_transcript(transcript_file, f"{dataset_name}-{partition}")

        segment_file = f"{folder_path}/transcription/{partition}/segments"
        utt2spk_file = f"{folder_path}/transcription/{partition}/utt2spk"
        utt2dur_file = f"{folder_path}/transcription/{partition}/utt2dur"
        wav_scp_file = f"{folder_path}/transcription/{partition}/wav.scp"
        audio_folder = f"{folder_path}/Audio"
        audio_rel_folder = f"~/{os.path.relpath(audio_folder, home_path)}"

        #Creating text
        target_text_file = f"{target_folder}/text"
        print(f"Writing text to {target_text_file}")

        # continue
        with open(target_text_file, "w") as t_file:
            t_file.write('\n'.join(processed_text_lines))

        if(dataset_name == "iitm_asr"):
            continue

            
        with open(transcript_file, "r") as t_file:
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
    # mozilla_path = "tamil_db_files/dataset_files/commonvoice_tamil"
    # mozilla_dataset_name = "mozilla"
    # create_files(mozilla_path, mozilla_dataset_name)
    # openslr_path = "~/kaldi/egs/tamil_telugu_proj/s5_r3/db/openslr_tamil"
    # openslr_path = "tamil_db_files/dataset_files/openslr_tamil"
    # openslr_dataset_name = "openslr"
    # create_files(openslr_path, openslr_dataset_name)
    #create_files(openslr_path, openslr_dataset_name)
    # mozilla_path = "~/kaldi/egs/tamil_telugu_proj/s5_r3/db/mozillacv_tamil"
    # mozilla_dataset_name = "mozilla"
    # create_files(mozilla_path, mozilla_dataset_name)
    # microsoft_path = "~/kaldi/egs/tamil_telugu_proj/s5_r3/db/microsoft_tamil"
    # microsoft_path = "tamil_db_files/dataset_files/microsoft_tamil"
    # microsoft_dataset_name = "microsoft"
    # create_files(microsoft_path, microsoft_dataset_name)
    # ittm_asr_path = "tamil_db_files/dataset_files/iitm_asr_tamil"
    # iitm_dataset_name = "iitm_asr"
    # create_files(ittm_asr_path, iitm_dataset_name)

    microsoft_dataset_name = "microsoft"
    microsoft_telugu_path = "~/kaldi/egs/tamil_telugu_proj/s5_r3/db/microsoft_telugu"
    openslr_telugu = "~/kaldi/egs/tamil_telugu_proj/s5_r3/db/openslr_telugu"
    openslr_dataset_name = "openslr"

    # create_files_telugu(openslr_telugu, openslr_dataset_name)
    create_files(microsoft_telugu_path, microsoft_dataset_name)
    # print("finished")

