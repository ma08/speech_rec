sk5057@speech-rec-vm:~/dataset/cv-corpus-8.0-2022-01-19/ta/clips$ soxi common_voice_ta_26484381.mp3

Input File     : 'common_voice_ta_26484381.mp3'
Channels       : 1
Sample Rate    : 32000
Precision      : 16-bit
Duration       : 00:00:09.86 = 315648 samples ~ 739.8 CDDA sectors
File Size      : 59.3k
Bit Rate       : 48.1k
Sample Encoding: MPEG audio (layer I, II or III)


sk5057@speech-rec-vm:~/dataset/cv-corpus-8.0-2022-01-19/ta/wavclips$ soxi common_voice_ta_19071679.wav 

Input File     : 'common_voice_ta_19071679.wav'
Channels       : 1
Sample Rate    : 16000
Precision      : 16-bit
Duration       : 00:00:06.65 = 106368 samples ~ 498.6 CDDA sectors
File Size      : 213k
Bit Rate       : 256k
Sample Encoding: 16-bit Signed Integer PCM

## Number of files in CommonVoice Tamil
sk5057@speech-rec-vm:~/dataset/cv-corpus-8.0-2022-01-19/ta/clips$ ls -l | wc -l
197734

## Number of files in microsoft Tamil 
sk5057@speech-rec-vm:~/asr_project/datasets$ ls -l microsoftspeechcorpusindianlanguages/ta-in-Train/Audios/ | wc -l
39132




with     sox -G "$i" -r 16k -e signed-integer "wavclips/$(basename -s .mp3 "$i").wav"



sk5057@speech-rec-vm:~/dataset/cv-corpus-8.0-2022-01-19/ta$ soxi wavclips/common_voice_ta_25563782.wav

Input File     : 'wavclips/common_voice_ta_25563782.wav'
Channels       : 1
Sample Rate    : 16000
Precision      : 16-bit
Duration       : 00:00:08.03 = 128448 samples ~ 602.1 CDDA sectors
File Size      : 257k
Bit Rate       : 256k
Sample Encoding: 16-bit Signed Integer PCM



sk5057@speech-rec-vm:~/dataset/cv-corpus-8.0-2022-01-19/ta$ cat convert_mp3towav_error.log  | grep "clipped" | wc -l
108

sk5057@speech-rec-vm:~/asr_project/datasets/cv-corpus-8.0-2022-01-19/ta/wavclips$ soxi common_voice_ta_25966716.wav

Input File     : 'common_voice_ta_25966716.wav'
Channels       : 1
Sample Rate    : 16000
Precision      : 16-bit
Duration       : 00:00:05.94 = 95040 samples ~ 445.5 CDDA sectors
File Size      : 190k
Bit Rate       : 256k
Sample Encoding: 16-bit Signed Integer PCM

##Extract zip to a folder
sk5057@speech-rec-vm:~/asr_project/datasets/openslr_tamil$ unzip ta_in_female.zip -d ta_in_female


## Created python script to calculate statistics of wavs in a directory
### Microsoft Tamil Train
sk5057@speech-rec-vm:~/asr_project/datasets$ python3 dataset_repo_folder/total_time_indir.py microsoftspeechcorpusindianlanguages/ta-in-Train/Audios/ | tee dataset_repo_folder/microsoftspeechcorpusindianlanguages_ta_duration.log 

1000 files processed
.
.
.
39000 files processed
Total number of files: 39131
Total time in seconds: 144002.90806199904
Total time in minutes: 2400.048467699984
Total time in hours: 40.00080779499974
Minimum time: 0.325
Maximum time: 18.57
Average time: 3.680021161278757

As max is only 18.57, we need not split for this dataset
- text: the transcription as it is
- segments


sk5057@speech-rec-vm:~/dataset/microsoftspeechcorpusindianlanguages/ta-in-Train/Audios$ soxi 001990001.wav 

Input File     : '001990001.wav'
Channels       : 1
Sample Rate    : 16000
Precision      : 16-bit
Duration       : 00:00:04.64 = 74240 samples ~ 348 CDDA sectors
File Size      : 149k
Bit Rate       : 256k
Sample Encoding: 16-bit Signed Integer PCM




### Microsoft Tamil Test
sk5057@speech-rec-vm:~/asr_project/datasets$ python3 dataset_repo_folder/total_time_in_dir.py microsoftspeechcorpusindianlanguages/ta-in-Test/Audios/ | tee dataset_repo_folder/microsoftspeechcorpusindianlanguages_ta_test_duration.log 
1000 files processed
2000 files processed
3000 files processed
Total number of files: 3081
Total time in seconds: 18009.220061999986
Total time in minutes: 300.15366769999974
Total time in hours: 5.00256112833333
Minimum time: 1.71
Maximum time: 14.5
Average time: 5.84525156183057


### OpenSLR Tamil
As max is 17 seconds, no data split is needed
#### Male
sk5057@speech-rec-vm:~/asr_project/datasets$ python3 -u dataset_repo_folder/total_time_in_dir.py openslr_tamil/ta_in_male/ | tee dataset_repo_folder/logs/openslr_tamil_male_dur.log
1000 files processed
Total number of files: 1956
Total time in seconds: 11066.88001999997
Total time in minutes: 184.44800033333283
Total time in hours: 3.0741333388888803
Minimum time: 1.962667
Maximum time: 17.152
Average time: 5.6579141206543815

sk5057@speech-rec-vm:~/asr_project/datasets/openslr_tamil/ta_in_male$ soxi tag_07925_01975386315.wav

Input File     : 'tag_07925_01975386315.wav'
Channels       : 1
Sample Rate    : 48000
Precision      : 16-bit
Duration       : 00:00:05.80 = 278528 samples ~ 435.2 CDDA sectors
File Size      : 557k
Bit Rate       : 768k
Sample Encoding: 16-bit Signed Integer PCM



#### Female
sk5057@speech-rec-vm:~/asr_project/datasets$ python3 -u dataset_repo_folder/total_time_in_dir.py openslr_tamil/ta_in_female/ | tee dataset_repo_folder/logs/openslr_tamil_female_dur.log
1000 files processed
2000 files processed
Total number of files: 2335
Total time in seconds: 14437.034672999967
Total time in minutes: 240.61724454999947
Total time in hours: 4.010287409166658
Minimum time: 1.706667
Maximum time: 13.824
Average time: 6.182884228265511

### IITM ASR Challenge (https://sites.google.com/view/indian-language-asrchallenge/home?authuser=2)

#### Downloading the files
sk5057@speech-rec-vm:~/asr_project/datasets$ wget -r --user=asrchallenge --password=asr_iitm123 -U "" https://asr.iitm.ac.in/downloads/Indian_Language_Database/Tamil/
--2022-05-01 08:07:51--  https://asr.iitm.ac.in/downloads/Indian_Language_Database/Tamil/
Resolving asr.iitm.ac.in (asr.iitm.ac.in)... 103.158.43.230
Connecting to asr.iitm.ac.in (asr.iitm.ac.in)|103.158.43.230|:443... connected.

.
.


#### Tamil Train
sk5057@speech-rec-vm:~/asr_project/datasets$ python3 -u dataset_repo_folder/total_time_in_dir.py asr.iitm.ac.in/downloads/Indian_Language_Database/Tamil/Audio | tee dataset_repo_folder/logs/asriitm_Tamil_Audio_dur.log
1000 files processed
2000 files processed
.
.
.
28000 files processed
Total number of files: 28970
Total time in seconds: 413726.25743499293
Total time in minutes: 6895.437623916549
Total time in hours: 114.92396039860915
Minimum time: 2.089875
Maximum time: 849.6
Average time: 14.28119632153928


sk5057@speech-rec-vm:~/asr_project/datasets/asr.iitm.ac.in/downloads/Indian_Language_Database/Tamil$ soxi Audio/104_tam_10033_106334.wav

Input File     : 'Audio/104_tam_10033_106334.wav'
Channels       : 1
Sample Rate    : 16000
Precision      : 16-bit
Duration       : 00:00:08.73 = 139692 samples ~ 654.806 CDDA sectors
File Size      : 279k
Bit Rate       : 256k
Sample Encoding: 16-bit Signed Integer PCM


####Tamil Eval
sk5057@speech-rec-vm:~/asr_project/datasets$ python3 -u dataset_repo_folder/total_time_in_dir.py asr.iitm.ac.in/downloads/Indian_Language_Database/Tamil/Audio_eval | tee dataset_repo_folder/logs/asriitm_Tamil_Audio_eval_dur.log
Total number of files: 219
Total time in seconds: 15306.732000000007
Total time in minutes: 255.11220000000012
Total time in hours: 4.251870000000002
Minimum time: 25.84
Maximum time: 103.936
Average time: 69.89375342465756





###Mozilla Common Voice Tamil
sk5057@speech-rec-vm:~/asr_project/datasets$ python3 -u  dataset_repo_folder/total_time_indir.py cv-corpus-8.0-2022-01-19/ta/wavclips/ | tee dataset_repo_folder/cv-corpus-8.0-2022-01-19_ta_duration.log
1000 files processed
.
.
.
197000 files processed
Total number of files: 197733
Total time in seconds: 1222649.6676870075
Total time in minutes: 20377.494461450126
Total time in hours: 339.6249076908354
Minimum time: 0.036
Maximum time: 20.34
Average time: 6.18333645717714


### Tedlium
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3$ ./run.sh 
----------------------- Stage 1 begin: prepare data ---------------------------
utils/validate_data_dir.sh: Successfully validated data-directory data/dev.orig
utils/validate_data_dir.sh: Successfully validated data-directory data/test.orig
extend_segment_times.py: extended 268263 segments; fixed 183022 overlapping segments
utils/validate_data_dir.sh: Successfully validated data-directory data/train.orig
utils/data/get_utt2dur.sh: working out data/dev.orig/utt2dur from data/dev.orig/segments
utils/data/get_utt2dur.sh: computed data/dev.orig/utt2dur
utils/data/modify_speaker_info.sh: copied data from data/dev.orig to data/dev, number of speakers changed from 8 to 38
utils/validate_data_dir.sh: Successfully validated data-directory data/dev
utils/data/get_utt2dur.sh: working out data/test.orig/utt2dur from data/test.orig/segments
utils/data/get_utt2dur.sh: computed data/test.orig/utt2dur
utils/data/modify_speaker_info.sh: copied data from data/test.orig to data/test, number of speakers changed from 11 to 59
utils/validate_data_dir.sh: Successfully validated data-directory data/test
utils/data/get_utt2dur.sh: working out data/train.orig/utt2dur from data/train.orig/segments
utils/data/get_utt2dur.sh: computed data/train.orig/utt2dur
utils/data/modify_speaker_info.sh: copied data from data/train.orig to data/train, number of speakers changed from 2351 to 10334
utils/validate_data_dir.sh: Successfully validated data-directory data/train
----------------------- Stage 1 end: prepare data ---------------------------


sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data$ cd train
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/train$ ls
glm  reco2file_and_channel  segments  spk2utt  stm  text  utt2spk  wav.scp
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/train$ vim wav.scp 
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/train$ vim utt2spk 
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/train$ vim text 
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/train$ vim spk2utt 
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/train$ vim segments 
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/train$ 

sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/dev$ wc -l text 
507 text
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/dev$ cd ..
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data$ cd train
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/train$ wc -l text 
268263 text
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/train$ cd ..
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data$ cd test
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/test$ wc -l text 
1155 text
sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/data/test$ 

dev: 507
train: 268263
test: 1155



