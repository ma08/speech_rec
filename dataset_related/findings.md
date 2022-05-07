# Miscallaneous findings
### Preprocessing mozilla transcript
```
2022-05-06 04:59:54.847121 !mcvspeaker135-common_voice_ta_25352078	நிறுத்து நிறுத்து என உத்தரவு போடுகிறாள் சிந்தாഥணி
! culprit:!சிந்தாഥணி!
2022-05-06 04:59:54.847126 orig:!நிறுத்து நிறுத்து என உத்தரவு போடுகிறாள் சிந்தாഥணி! afterpunc:!நிறுத்து நிறுத்து என உத்தரவு போடுகிறாள் சிந்தாഥணி!
2022-05-06 04:59:54.847128 ------------
```
Here `சிந்தாഥணி` is failing Tamil word test because([source](https://www.babelstone.co.uk/Unicode/whatisit.html)):
```
U+0B9A : TAMIL LETTER CA
U+0BBF : TAMIL VOWEL SIGN I
U+0BA8 : TAMIL LETTER NA
U+0BCD : TAMIL SIGN VIRAMA {pulli}
U+0BA4 : TAMIL LETTER TA
U+0BBE : TAMIL VOWEL SIGN AA
U+0D25 : MALAYALAM LETTER THA {ttha}
U+0BA3 : TAMIL LETTER NNA
U+0BBF : TAMIL VOWEL SIGN I
```

```
2022-05-06 07:21:49.572011 !!!!!!!!!!!!!!!!!!!!
2022-05-06 07:21:49.572239 ------------
2022-05-06 07:21:49.572253 is_comb: False orig_wrod: !விsஹயம்! comb:!விsஹயம்!
2022-05-06 07:21:49.572256 not clean மற்றொரு முக்கிய விsஹயம் சமிக்ஞை உமிழ்வு கட்டுப்பாடு
2022-05-06 07:21:49.572259 ------------
2022-05-06 07:21:49.572326 !!!!!!!!!!!!!!!!!!!!

2022-05-06 07:21:49.583151 !!!!!!!!!!!!!!!!!!!!
2022-05-06 07:21:49.583254 ------------
2022-05-06 07:21:49.583269 is_comb: False orig_wrod: !நருடகிsouக்கு! comb:!நருடகிsouக்கு!
2022-05-06 07:21:49.583272 not clean இது தெரியாமல் ரியூஷி தனது கனவை நனவாக்க நருடகிsouக்கு நகர்கிறார்
2022-05-06 07:21:49.583275 ------------
2022-05-06 07:21:49.583364 !!!!!!!!!!!!!!!!!!!!
```

found duplicate window option in vscode!!!
https://stackoverflow.com/questions/49707703/open-the-same-directory-twice


### for mozilla
checked both unicode and ascii whitespace versions
```
2022-05-06 08:34:19.785776 Running on mozilla train
2022-05-06 08:34:19.785875 Processing tamil_db_files/dataset_files/commonvoice_tamil/train_transcription.txt for mozilla-train
2022-05-06 08:34:19.907522 not clean மற்றொரு முக்கிய விsஹயம் சமிக்ஞை உமிழ்வு கட்டுப்பாடு
2022-05-06 08:34:19.914632 not clean இது தெரியாமல் ரியூஷி தனது கனவை நனவாக்க நருடகிsouக்கு நகர்கிறார்
2022-05-06 08:34:20.174134 not clean நிறுத்து நிறுத்து என உத்தரவு போடுகிறாள் சிந்தாഥணி
2022-05-06 08:34:20.245159 pure_eng_lines_count: 1704
2022-05-06 08:34:20.245197 comb_word_lines_count: 259
2022-05-06 08:34:20.245200 whitespace_fixed_lines_count: 0
2022-05-06 08:34:20.245203 unclean_lines_count: 3
2022-05-06 08:34:20.245304 Writing text to tamil_db_files/dataset_files/commonvoice_tamil/transcription/train/text
2022-05-06 08:34:20.270663 Running on mozilla dev
2022-05-06 08:34:20.270767 Processing tamil_db_files/dataset_files/commonvoice_tamil/dev_transcription.txt for mozilla-dev
2022-05-06 08:34:20.295327 not clean காஃபி உலகில் விளையும் மொத்தக் காஃபியில் ¾ பங்கு பிரேசில் நாட்டில் விளைகிறது
2022-05-06 08:34:20.405266 pure_eng_lines_count: 31
2022-05-06 08:34:20.405327 comb_word_lines_count: 3
2022-05-06 08:34:20.405329 whitespace_fixed_lines_count: 0
2022-05-06 08:34:20.405332 unclean_lines_count: 1
2022-05-06 08:34:20.410141 Writing text to tamil_db_files/dataset_files/commonvoice_tamil/transcription/dev/text
2022-05-06 08:34:20.419496 Running on mozilla test
2022-05-06 08:34:20.419771 Processing tamil_db_files/dataset_files/commonvoice_tamil/test_transcription.txt for mozilla-test
2022-05-06 08:34:20.546698 not clean இதன் குறுக்களவு ½ கல் இருக்கும்
2022-05-06 08:34:20.566454 pure_eng_lines_count: 108
2022-05-06 08:34:20.566513 comb_word_lines_count: 13
2022-05-06 08:34:20.566517 whitespace_fixed_lines_count: 0
2022-05-06 08:34:20.566523 unclean_lines_count: 1
2022-05-06 08:34:20.568466 Writing text to tamil_db_files/dataset_files/commonvoice_tamil/transcription/test/text
```


### for openslr
```
2022-05-06 08:40:41.424709 not clean நட‌க்க முடியாதவ‌ர்க‌ள் ‌சிலரை அ‌ந்த வ‌ழியாக வ‌ந்தவ‌ர்க‌ள் த‌ங்களது வாகன‌த்‌தி‌ல் ஏ‌ற்‌றி ஊ‌ட்டி மு‌க்‌கிய சாலை‌க்கு கொ‌ண்டு வ‌ந்து ‌வி‌ட்டன‌ர்
2022-05-06 08:40:41.424739 culprit words ['நட\u200cக்க', 'முடியாதவ\u200cர்க\u200cள்', '\u200cசிலரை', 'அ\u200cந்த', 'வ\u200cழியாக', 'வ\u200cந்தவ\u200cர்க\u200cள்', 'த\u200cங்களது', 'வாகன\u200cத்\u200cதி\u200cல்', 'ஏ\u200cற்\u200cறி', 'ஊ\u200cட்டி', 'மு\u200cக்\u200cகிய', 'சாலை\u200cக்கு', 'கொ\u200cண்டு', 'வ\u200cந்து', '\u200cவி\u200cட்டன\u200cர்']
```
example: நட‌க்க is failing
```
U+0BA8 : TAMIL LETTER NA
U+0B9F : TAMIL LETTER TTA
U+200C : ZERO WIDTH NON-JOINER [ZWNJ]
U+0B95 : TAMIL LETTER KA
U+0BCD : TAMIL SIGN VIRAMA {pulli}
U+0B95 : TAMIL LETTER KA
```

```
sourya4@IWeighHar:~/pro/columbia/spring22/fund_sp_rec/speech_rec_repo/dataset_related$ python3 create_lexicon.py 
2022-05-06 08:53:05.515350 print(split_word_to_letters('நட‌க்க')): ['ந', 'ட', '\u200c', 'க்', 'க']
```

therefore removing

```
2022-05-06 08:56:49.522511 Running on openslr train
2022-05-06 08:56:49.522592 Processing tamil_db_files/dataset_files/openslr_tamil/train_transcription.txt for openslr-train
2022-05-06 08:56:49.561949 not clean சிலர் நீங்கள் முன்பு போல் இல்லையென்றும் மாறி விட்டதாகவும் கூறுவார்கள்taf_02345_00348037167 ஆஸ்த்ரேலியப் பெண்ணுக்கு முப்பத்தி மூன்று ஆண்டுகளுக்குப் பின்னர் இந்தியா இழப்பீடு வழங்கியது
2022-05-06 08:56:49.561979 culprit words ['கூறுவார்கள்taf0234500348037167']
```
Taking care of alpha numeric instead of just alpha now

### iitm asr
```
2022-05-06 09:23:52.599056 Running on iitm_asr train
2022-05-06 09:23:52.599129 Processing tamil_db_files/dataset_files/iitm_asr_tamil/train_transcription.txt for iitm_asr-train
2022-05-06 09:23:53.410978 not clean மார்க்கெட்டிங் அதிகாரி﻿ சந்தைப்படுத்துதலுக்கு இன்று அத்தனை துறைகளும்
2022-05-06 09:23:53.411024 culprit words ['அதிகாரி\ufeff']
2022-05-06 09:23:53.416826 not clean தோல்வி அடைந்ததாகக் கூறப்படுவது குறித்து﻿ இதுபோல் ஒரு முயற்சி நடைபெறவில்லை தான்
2022-05-06 09:23:53.416851 culprit words ['குறித்து\ufeff']
2022-05-06 09:23:53.442846 pure_eng_lines_count: 24
2022-05-06 09:23:53.442868 comb_word_lines_count: 0
2022-05-06 09:23:53.442871 whitespace_fixed_lines_count: 0
2022-05-06 09:23:53.442873 unclean_lines_count: 2
```

added it to the pronounciation function

```
2022-05-06 09:58:35.289490 Running on iitm_asr train
2022-05-06 09:58:35.289577 Processing tamil_db_files/dataset_files/iitm_asr_tamil/train_transcription.txt for iitm_asr-train
2022-05-06 09:58:36.135770 pure_eng_lines_count: 24
2022-05-06 09:58:36.135790 comb_word_lines_count: 0
2022-05-06 09:58:36.135792 whitespace_fixed_lines_count: 0
2022-05-06 09:58:36.135795 unclean_lines_count: 0
2022-05-06 09:58:36.135848 Writing text to tamil_db_files/dataset_files/iitm_asr_tamil/transcription/train/text
2022-05-06 09:58:36.135851 Running on iitm_asr dev
2022-05-06 09:58:36.135908 Processing tamil_db_files/dataset_files/iitm_asr_tamil/dev_transcription.txt for iitm_asr-dev
2022-05-06 09:58:36.172441 pure_eng_lines_count: 0
2022-05-06 09:58:36.172459 comb_word_lines_count: 0
2022-05-06 09:58:36.172462 whitespace_fixed_lines_count: 0
2022-05-06 09:58:36.172464 unclean_lines_count: 0
2022-05-06 09:58:36.176327 Writing text to tamil_db_files/dataset_files/iitm_asr_tamil/transcription/dev/text
2022-05-06 09:58:36.176346 Running on iitm_asr test
2022-05-06 09:58:36.176411 Processing tamil_db_files/dataset_files/iitm_asr_tamil/test_transcription.txt for iitm_asr-test
2022-05-06 09:58:36.212548 pure_eng_lines_count: 1
2022-05-06 09:58:36.212568 comb_word_lines_count: 1
2022-05-06 09:58:36.212570 whitespace_fixed_lines_count: 0
2022-05-06 09:58:36.212572 unclean_lines_count: 0
2022-05-06 09:58:36.212834 Writing text to tamil_db_files/dataset_files/iitm_asr_tamil/transcription/test/text
```
