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
  


