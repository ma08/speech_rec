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
2022-05-06 07:51:22.606127 Running on mozilla train
2022-05-06 07:51:22.606206 Processing tamil_db_files/dataset_files/commonvoice_tamil/train_transcription.txt for mozilla-train
2022-05-06 07:51:22.772602 not clean மற்றொரு முக்கிய விsஹயம் சமிக்ஞை உமிழ்வு கட்டுப்பாடு
2022-05-06 07:51:22.783631 not clean இது தெரியாமல் ரியூஷி தனது கனவை நனவாக்க நருடகிsouக்கு நகர்கிறார்
2022-05-06 07:51:23.130154 not clean நிறுத்து நிறுத்து என உத்தரவு போடுகிறாள் சிந்தாഥணி
2022-05-06 07:51:23.219460 pure_eng_lines_count: 1704
2022-05-06 07:51:23.219500 comb_word_lines_count: 259
2022-05-06 07:51:23.219503 whitespace_fixed_lines_count: 0
2022-05-06 07:51:23.219605 Running on mozilla dev
2022-05-06 07:51:23.219758 Processing tamil_db_files/dataset_files/commonvoice_tamil/dev_transcription.txt for mozilla-dev
2022-05-06 07:51:23.250791 not clean காஃபி உலகில் விளையும் மொத்தக் காஃபியில் ¾ பங்கு பிரேசில் நாட்டில் விளைகிறது
2022-05-06 07:51:23.382265 pure_eng_lines_count: 31
2022-05-06 07:51:23.382321 comb_word_lines_count: 3
2022-05-06 07:51:23.382324 whitespace_fixed_lines_count: 0
2022-05-06 07:51:23.382343 Running on mozilla test
2022-05-06 07:51:23.382538 Processing tamil_db_files/dataset_files/commonvoice_tamil/test_transcription.txt for mozilla-test
2022-05-06 07:51:23.505246 not clean இதன் குறுக்களவு ½ கல் இருக்கும்
2022-05-06 07:51:23.530538 pure_eng_lines_count: 108
2022-05-06 07:51:23.530578 comb_word_lines_count: 13
2022-05-06 07:51:23.530581 whitespace_fixed_lines_count: 0
```