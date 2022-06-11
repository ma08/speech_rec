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


