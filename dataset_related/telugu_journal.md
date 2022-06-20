## Data preprocessing
### Microsoft Telugu
- create dev from train using split_dataset.py (1%)
- Shuffling in split_dataset.py messing up with sort order in kaldi validation?
- Found vscode bug... new file created not being updated (split)
- Realized the split was using only 1% of train file to create dev. changed it to 10%
  - check if we should do the same for tamil? TODO

### Openslr Telugu
- Removed \n from end of lines
- Removed _letter stuff from acronyms
- changed split to 10% 10% for dev and test instead of 1% and 1%
- Run split_dataset

### Preprocessing
- Normalization
  - /home/sourya4/pro/repos/indic_nlp_resources
  - export INDIC_RESOURCES_PATH=/home/sourya4/pro/repos/indic_nlp_resources
  - Found documentation mistake in https://anoopkunchukuttan.github.io/indic_nlp_library/
    - `normalizer=factory.get_normalizer("hi",remove_nuktas)` should be  ``normalizer=factory.get_normalizer("hi",remove_nuktas=remove_nutkas)`
  - Created a module to get count of normalizations through the library
    - stored logs in logs/normalization_logs
	- Tamil: 1.6% (across all datasets)
	- Telugu: 0.03%
  - Going ahead and running telugu without normalizing (not worth the effort?)

- Validation of pure telugu
  - stored count and illegal word logs in logs/transcript_validation (for tamil too)
    - For tamil, removing of characters like U+200c : ZERO WIDTH NON-JOINER from corpus affected ? TODO: verify
    - For telugu, removing illegal characters including zero width non-joiner
      - created clean_transcript module
        - removing punctuation using function utility
        - removing few by hand to save time
          - & -> అన్డ్
          - tem_07220_01981175708	 (removed)
          - GPS -> జిపిఎస్ 
        - fix whitespace?
      - should do same for corpus for lang model as well
      - created new transcripts
      - obtained 0 illegal counts through validation after preprocessing
        ```
        sourya4@IWeighHar:~/pro/columbia/spring22/fund_sp_rec/speech_rec_repo/dataset_related$ python3 clean_transcript.py > logs/telugu_transcript_preprocess3.log
        sourya4@IWeighHar:~/pro/columbia/spring22/fund_sp_rec/speech_rec_repo/dataset_related$ python3 validate_transcript.py > logs/telugu_processed.count.log
        ```
- create data files
  - create audio folders and move to db/ (same recipe folder used for tamil )
    - microsoft_telugu/Audio
    - openslr_telugu/Audio
  - Update create_data_files for telugu
  - Oops. Ran with old function (Tamil) for openslr_Telugu. Checked if text file got messed. Didnt.
  - Checking audio format
    - #openslr
      ```
      sk5057@speech-rec-vm:~/kaldi/egs/tamil_telugu_proj/s5_r3/db/openslr_telugu/Audio$ soxi tef_01033_00007107192.wav

      Input File     : 'tef_01033_00007107192.wav'
      Channels       : 1
      Sample Rate    : 48000
      Precision      : 16-bit
      Duration       : 00:00:03.84 = 184320 samples ~ 288 CDDA sectors
      File Size      : 369k
      Bit Rate       : 768k
      Sample Encoding: 16-bit Signed Integer PCM
      ```
    - #microsoft
      ```
      sk5057@speech-rec-vm:~/kaldi/egs/tamil_telugu_proj/s5_r3/db/microsoft_telugu/Audio$ soxi 000010007.wav

      Input File     : '000010007.wav'
      Channels       : 1
      Sample Rate    : 16000
      Precision      : 16-bit
      Duration       : 00:00:03.94 = 63040 samples ~ 295.5 CDDA sectors
      File Size      : 126k
      Bit Rate       : 256k
      Sample Encoding: 16-bit Signed Integer PCM
      ```
    - found that openslr has 48khz
      - convert it to 16khz. created convert_samplerate.sh and ran on openslr_telugu and copied to db
        ```
        sk5057@speech-rec-vm:~/kaldi/egs/tamil_telugu_proj/s5_r3/db/openslr_telugu/Audio$ soxi tef_01033_00007107192.wav

        Input File     : 'tef_01033_00007107192.wav'
        Channels       : 1
        Sample Rate    : 16000
        Precision      : 16-bit
        Duration       : 00:00:03.84 = 61440 samples ~ 288 CDDA sectors
        File Size      : 123k
        Bit Rate       : 256k
        Sample Encoding: 16-bit Signed Integer PCM
        ```
        TODO: check audio quality
      - found that for tamil.... openslr has 48khz.. it seems we have used the audio without as it is. without changing. have to rerun it?
    - create spk2utt using script for both
    - merge
      - https://stackoverflow.com/questions/12616039/wc-command-of-mac-showing-one-less-result
      - removed empty lines at end of files manually
- Create lexicon
  - found method in indic nlp library which gives orthographic for all indic languages
    - installed library and resrouces in VM
    - created method in utility module
      ```
      sk5057@speech-rec-vm:~/asr_project/git_repo/dataset_related$ python3 create_lexicon.py 
      2022-06-12 22:17:54.736687 Total words: 295642, non telugu count 1 set count: 49169
      ```
    - add validate method for lexicon in create_lexicon module
    - lexicon for telugu done
      - TODO: use same method for tamil and verify difference?

## telugu_run.sh
- Create telugu_run.sh for telugu
- change paths in stages and change other files as required
- setup git lfs
  - using db/.gitattributes
  ```
  data/** filter=lfs diff=lfs merge=lfs -text
  data/**/* filter=lfs diff=lfs merge=lfs -text
  telugu_data/** filter=lfs diff=lfs merge=lfs -text
  telugu_data/** filter=lfs diff=lfs merge=lfs -text
  ```

### stage 0

nohup ./run_telugu.sh > telugu_logs/stage0.log 2>&1 &

### stage 1

nohup ./run_telugu.sh > telugu_logs/stage1.log 2>&1 &

### stage 2
nohup ./run_telugu.sh > telugu_logs/stage2.log 2>&1 &
tail -f telugu_logs/stage2.log

### stage 3
nohup ./run_telugu.sh > telugu_logs/stage3.log 2>&1 &
tail -f telugu_logs/stage3.log

### stage 4

#### Text processing for language model
- create telugu version of preprocessing scripts
nohup ./clean_corpus_telugu.sh te.txt > telugu_clean.log 2>&1 &
nohup ./clean_corpus_telugu.sh  > telugu_clean1.log 2>&1 &
```
sk5057@speech-rec-vm:~/asr_project/git_repo/lang_model/preprocessing$ gzip -c stage5_out_telugu.txt > ~/kaldi/egs/tamil_telugu_proj/s5_r3/db/telugu_text_processed.txt.gz

```




nohup ./run_telugu.sh > telugu_logs/stage4.log 2>&1 &
tail -f telugu_logs/stage4.log

- Setup git lfs for telugu_data versioning... couldn't add .txt.gz due to > 2GB. Added dummy file
-
### stage 5  
nohup ./run_telugu.sh > telugu_logs/stage5.log 2>&1 &
tail -f telugu_logs/stage5.log

adding changes to db repo as well

### stage 6  
nohup ./run_telugu.sh > telugu_logs/stage6.log 2>&1 &
tail -f telugu_logs/stage6.log

1 less in logs?



### stage 7  
nohup ./run_telugu.sh > telugu_logs/stage7.log 2>&1 &
tail -f telugu_logs/stage7.log

### stage 8  
nohup ./run_telugu.sh > telugu_logs/stage7.log 2>&1 &
tail -f telugu_logs/stage7.log

### stage 8  

### stage 9  

### stage 10  
nohup ./run_telugu.sh > telugu_logs/stage10.log 2>&1 &
tail -f telugu_logs/stage10.log


error 

https://groups.google.com/g/kaldi-help/c/b9os_OyHLvc

run out of ram?
  found that it was taking 50/50g
  switched to n1-highmem-16 104gb ram and trying
    went upto 61G
    success!!

### stage 11  
using same config as above
nohup ./run_telugu.sh > telugu_logs/stage11.log 2>&1 &
tail -f telugu_logs/stage11.log

### stage 12  
using same config as above
nohup ./run_telugu.sh > telugu_logs/stage12.log 2>&1 &
tail -f telugu_logs/stage12.log

### stage 13  
using same config as above
nohup ./run_telugu.sh > telugu_logs/stage13.log 2>&1 &
tail -f telugu_logs/stage13.log

### stage 14  
using same config as above
nohup ./run_telugu.sh > telugu_logs/stage14.log 2>&1 &
tail -f telugu_logs/stage14.log

### stage 15  
back to old config
nohup ./run_telugu.sh > telugu_logs/stage15.log 2>&1 &
tail -f telugu_logs/stage15.log

### stage 16  
using same config as above
nohup ./run_telugu.sh > telugu_logs/stage16.log 2>&1 &
tail -f telugu_logs/stage16.log

### stage 17  
sudo nvidia-smi -c 3 ?? should we run this. running
```
root@speech-rec-vm:/home/sk5057_columbia_edu# nvidia-smi -c 3
Set compute mode to EXCLUSIVE_PROCESS for GPU 00000000:00:04.0.
All done.
```


sk5057@speech-rec-vm:~/kaldi/egs/tamil_telugu_proj/s5_r3$ nvidia-smi
Tue Jun 14 17:01:39 2022       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.129.06   Driver Version: 470.129.06   CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla K80           Off  | 00000000:00:04.0 Off |                    0 |
| N/A   41C    P0    64W / 149W |      0MiB / 11441MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+


nohup ./run_telugu.sh > telugu_logs/stage17.log 2>&1 &
tail -f telugu_logs/stage17.log


```
sk5057@speech-rec-vm:~/kaldi/src/nnet3bin$ ./cuda-gpu-available 
LOG ([5.5.1009~1-e4940]:main():cuda-gpu-available.cc:61) 

### IS CUDA GPU AVAILABLE? 'speech-rec-vm' ###
ERROR ([5.5.1009~1-e4940]:SelectGpuId():cu-device.cc:181) No CUDA GPU detected!, diagnostics: cudaError_t 30 : "unknown error", in cu-device.cc:181

[ Stack-Trace: ]
./cuda-gpu-available(kaldi::MessageLogger::LogMessage() const+0xb61) [0x563bc1e36f01]
./cuda-gpu-available(kaldi::MessageLogger::LogAndThrow::operator=(kaldi::MessageLogger const&)+0x21) [0x563bc1d2c47f]
./cuda-gpu-available(kaldi::CuDevice::SelectGpuId(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)+0x40f) [0x563bc1d2b64b]
./cuda-gpu-available(main+0x1b6) [0x563bc1d25481]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xe7) [0x7f60c9e5cc87]
./cuda-gpu-available(_start+0x2a) [0x563bc1d2512a]

kaldi::KaldiFatalError
LOG ([5.5.1009~1-e4940]:main():cuda-gpu-available.cc:97) ...
### WE DID NOT GET A CUDA GPU!!! ###
### If your system has a 'free' CUDA GPU, try re-installing latest 'CUDA toolkit' from NVidia (this updates GPU drivers too).
### Otherwise 'nvidia-smi' shows the status of GPUs:
### - The versions should match ('NVIDIA-SMI' and 'Driver Version'), otherwise reboot or reload kernel module,
### - The GPU should be unused (no 'process' in list, low 'memory-usage' (<100MB), low 'gpu-fan' (<30%)),
### - You should see your GPU (burnt GPUs may disappear from the list until reboot),
```



```
root@speech-rec-vm:/home/sk5057/kaldi/src/nnet3bin# ./cuda-gpu-available 
LOG ([5.5.1009~1-e4940]:main():cuda-gpu-available.cc:61) 

### IS CUDA GPU AVAILABLE? 'speech-rec-vm' ###
LOG ([5.5.1009~1-e4940]:SelectGpuId():cu-device.cc:238) CUDA setup operating under Compute Exclusive Mode.
LOG ([5.5.1009~1-e4940]:FinalizeActiveGpu():cu-device.cc:338) The active GPU is [0]: Tesla K80	free:11313M, used:127M, total:11441M, free/total:0.988856 version 3.7
### HURRAY, WE GOT A CUDA GPU FOR COMPUTATION!!! ##

### Testing CUDA setup with a small computation (setup = cuda-toolkit + gpu-driver + kaldi):
### Test OK!
root@speech-rec-vm:/home/sk5057/kaldi/src/nnet3bin# exit
exit
sk5057_columbia_edu@speech-rec-vm:~$ sudo su
root@speech-rec-vm:/home/sk5057_columbia_edu# su sk5057
sk5057@speech-rec-vm:/home/sk5057_columbia_edu$ /home/sk5057/kaldi/src/nnet3bin
bash: /home/sk5057/kaldi/src/nnet3bin: Is a directory
sk5057@speech-rec-vm:/home/sk5057_columbia_edu$ cd /home/sk5057/kaldi/src/nnet3bin
sk5057@speech-rec-vm:~/kaldi/src/nnet3bin$ ./cuda-gpu-available 
LOG ([5.5.1009~1-e4940]:main():cuda-gpu-available.cc:61) 

### IS CUDA GPU AVAILABLE? 'speech-rec-vm' ###
LOG ([5.5.1009~1-e4940]:SelectGpuId():cu-device.cc:238) CUDA setup operating under Compute Exclusive Mode.
LOG ([5.5.1009~1-e4940]:FinalizeActiveGpu():cu-device.cc:338) The active GPU is [0]: Tesla K80	free:11313M, used:127M, total:11441M, free/total:0.988856 version 3.7
### HURRAY, WE GOT A CUDA GPU FOR COMPUTATION!!! ##

### Testing CUDA setup with a small computation (setup = cuda-toolkit + gpu-driver + kaldi):
### Test OK!
```
- for some reason when same is run with root, it started working :/


Got results in the range of 17-24% WER
