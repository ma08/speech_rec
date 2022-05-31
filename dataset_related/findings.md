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

### microsoft kaldi db diff
```
sk5057@speech-rec-vm:~/asr_project/git_repo/dataset_related$ python3 -u create_data_files.py | tee ../kaldi_tamtel_db/logs/microsoft_proprocess_1.log 
2022-05-07 06:39:15.678151 Running on microsoft train
2022-05-07 06:39:15.678546 Processing /home/sk5057/kaldi/egs/tamil_telugu_proj/s5_r3/db/microsoft_tamil/train_transcription.txt for microsoft-train
2022-05-07 06:39:16.340196 pure_eng_lines_count: 0
2022-05-07 06:39:16.340253 comb_word_lines_count: 0
2022-05-07 06:39:16.340261 unclean_lines_count: 0
2022-05-07 06:39:16.340342 Writing text to /home/sk5057/kaldi/egs/tamil_telugu_proj/s5_r3/db/microsoft_tamil/transcription/train/text
2022-05-07 06:41:49.070982 Running on microsoft dev
2022-05-07 06:41:49.071289 Processing /home/sk5057/kaldi/egs/tamil_telugu_proj/s5_r3/db/microsoft_tamil/dev_transcription.txt for microsoft-dev
2022-05-07 06:41:49.077669 pure_eng_lines_count: 0
2022-05-07 06:41:49.077710 comb_word_lines_count: 0
2022-05-07 06:41:49.077717 unclean_lines_count: 0
2022-05-07 06:41:49.083199 Writing text to /home/sk5057/kaldi/egs/tamil_telugu_proj/s5_r3/db/microsoft_tamil/transcription/dev/text
2022-05-07 06:41:50.788101 Running on microsoft test
2022-05-07 06:41:50.788405 Processing /home/sk5057/kaldi/egs/tamil_telugu_proj/s5_r3/db/microsoft_tamil/test_transcription.txt for microsoft-test
2022-05-07 06:41:50.854178 pure_eng_lines_count: 0
2022-05-07 06:41:50.854230 comb_word_lines_count: 0
2022-05-07 06:41:50.854240 unclean_lines_count: 0
2022-05-07 06:41:50.854416 Writing text to /home/sk5057/kaldi/egs/tamil_telugu_proj/s5_r3/db/microsoft_tamil/transcription/test/text

```
but had punctuation stuff
```
-001780406      முதல்வர் ஜெயலலிதா, அவரது தோழி சசிகலா, சுதாகரன், இளவரசி ஆகியோர் மீதான சொத்து குவிப்பு வழக்கு பெங்களூர் சிறப்பு நீதிமன்றத்தில் நடந்து வருகிறது
+001780406      முதல்வர் ஜெயலலிதா அவரது தோழி சசிகலா சுதாகரன் இளவரசி ஆகியோர் மீதான சொத்து குவிப்பு வழக்கு பெங்களூர் சிறப்பு நீதிமன்றத்தில் நடந்து வருகிறது
 TA0509-TA0510_2-A.101  ஓகே
 000530482      தமிழக முதல்வர் கருணாநிதி இது தொடர்பாக இலங்கை அரசுக்கு கண்டனம் தெரிவித்திருந்தார்
 002010006      ஜெயலலிதா என்றாவது தனி நபராக காவேரி பிரச்சனையில் மனு தாக்கல் செய்தாரா என்று
@@ -478,11 +478,11 @@ TA0533-TA0534_1-B.141     ஆமா
 TA0725-TA0727_2-B.310  இப்போ
 000510256      இருவரும் லஷ்கர் இ தொய்பா தீவிரவாத இயக்கத்தை சேர்ந்தவர்கள் என தெரியவந்தது
 TA0343-TA0344_2-B.019  அக்கா இங்க வாங்க
-000880117      மிக வலுவான இந்திய கபடி அணி, தொடரட்டும் வெற்றி
+000880117      மிக வலுவான இந்திய கபடி அணி தொடரட்டும் வெற்றி

-000880117      மிக வலுவான இந்திய கபடி அணி, தொடரட்டும் வெற்றி
+000880117      மிக வலுவான இந்திய கபடி அணி தொடரட்டும் வெற்றி
 TA0337-TA0339_1-A.126  ஆமா
 TA0470-TA0472_2-A.262  ஆமா
 002350150      நான் ஏமாளியாகக் கூடாது என்பதற்காக அடுத்தவனை திருடனாக உருவாக்கிறேன்
-000870322      தாங்கள் நேரடி அரசியலுக்கு வந்து மக்களுக்கு சேவை செய்ய விருப்பம் உள்ளதா?
sk5057@speech-rec-vm:~/kaldi/egs/tamil_telugu_proj/s5_r3/db/microsoft_tamil/transcription/train$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   ../dev/text
	modified:   ../test/text
	modified:   text

no changes added to commit (use "git add" and/or "git commit -a")
sk5057@speech-rec-vm:~/kaldi/egs/tamil_telugu_proj/s5_r3/db/microsoft_tamil/transcription/train$ git diff --shortstat
 3 files changed, 4132 insertions(+), 4132 deletions(-)


```
 
### openslr kalsi asr db
```
 taf_01484_00026235194  ஜனவரி மாத கடைசியில் எந்தவித முன் அறிவிப்பும் இல்லாமல் திருச்செந்தூருக்கான சிறப்பு ரயில்களை நிறுத்திவிட்டனர்
-taf_01484_00033474579  நட<U+200C>க்க முடியாதவ<U+200C>ர்க<U+200C>ள் <U+200C>சிலரை அ<U+200C>ந்த வ<U+200C>ழியாக வ<U+200C>ந்தவ<U+200C>ர்க<U+200C>ள் த<U+200C>ங்களது வாகன<U+200C>த்<U+200C>தி<U+200C>ல் ஏ<U+200C>ற்<U+200C>றி ஊ<U+200C>ட்டி மு<U+200C>க்<U+200C>கிய சாலை<U+200C>க்கு கொ<U+200C>ண்டு வ<U+200C>ந்து <U+200C>வி<U+200C>ட்டன
<U+200C>ர்
+taf_01484_00033474579  நடக்க முடியாதவர்கள் சிலரை அந்த வழியாக வந்தவர்கள் தங்களது வாகனத்தில் ஏற்றி ஊட்டி முக்கிய சாலைக்கு கொண்டு வந்து விட்டனர்
 taf_01484_00037802472  ஆறாம் விக்கெட்டுக்கான ஓட்டக் குவிப்பில் இலங்கை வீரர்கள் உலக சாதனை
-taf_01484_00064157101  விகடன் டாக்கீஸ் தயா<U+200C>ரித்திருக்கும் இந்தப் படத்துக்கு இளைஞர்கள் மத்தியில் நல்ல வரவேற்பு
+taf_01484_00064157101  விகடன் டாக்கீஸ் தயாரித்திருக்கும் இந்தப் படத்துக்கு இளைஞர்கள் மத்தியில் நல்ல வரவேற்பு
 taf_01484_00232196777  ரொம்ப வருஷமா இந்த நாளுக்காகத்தான் காத்திருந்தேன் அதர்வா பேட்டி
 taf_01484_00234163212  அவரது திரைவாழ்க்கையில் முக்கியமான திரைப்படமாக தி சைலன்ஸ் கருதப்படுகிறது
 taf_01484_00241460648  உச்ச நீதிமன்றத்தில் அம்பானி சகோதரர்கள் விவகாரம்
@@ -100,7 +100,7 @@ taf_01484_00396152748       டிசம்பர் மூன்று உலக ம
 taf_01484_00397439171  அஜித்தின் நடிப்பு எப்படி
 taf_01484_00445628547  டா வின்சி வரைந்த ஓவியம் ஒன்று புதிதாக அடையாளம் காணப்பட்டது
 taf_01484_00457895890  அங்கோலா விமான விபத்தில் உயர் இராணுவ அதிகாரிகள் உயிரிழப்பு
-taf_01484_00536227138  கா<U+200C>ரி<U+200C>ல் அம<U+200C>ர்<U+200C>ந்தபடியே மெ<U+200C>ரினா கட<U+200C>ற்கரை
<U+200C>யி<U+200C>ல் அமை<U+200C>க்<U+200C>க<U+200C>ப்ப<U+200C>ட்டு<U+200C>ள்ள <U+200C>சிற<U+200C>ப்பு<U+200C>ப் ப<U+200C>ணிகளை ஆ<U+200C>ர்வ<U+200C>த்துட<U+200C>ன் சு<U+200C>ற்<U+200C>றி<U+200C>ப்பா<U+200C>ர்<U+200C>த்தா
<U+200C>ர்
+taf_01484_00536227138  காரில் அமர்ந்தபடியே மெரினா கடற்கரையில் அமைக்கப்பட்டுள்ள சிறப்புப் பணிகளை ஆர்வத்துடன் சுற்றிப்பார்த்தார்
 taf_01484_00593881433  சிவசங்கருக்கும் அரிதாசுக்கும் நீச்சல் தெரியாது
 taf_01484_00594900440  ரோகித் ஒரு ரன் எடுத்தார்
 taf_01484_00650995582  கொங்கோவில் எரிமலை சீற்றத்தால் அரிதான சிம்பன்சிகளுக்கு ஆபத்து
@@ -114,12 +114,12 @@ taf_01484_00737375974     பதினொன்று பேருக்கு ம
 taf_01484_00743436614  எந்திரன் டூ நேற்று அதிகாரப்பூர்வமாக தொடங்கப்பட்டது
 taf_01484_00751471407  தார்பூர் பிராந்திய ஆணையம் அமைக்க சூடான் முடிவு
 taf_01484_00771428067  அமெரிக்காவில் ஒளிபரப்பாகும் தொலைக்காட்சி தொடர் ஒன்றில் ப்ரியங்கா நடித்து வருகிறார்
-taf_01484_00774826591  சமீபத்தில் எந்த ஒரு த்<U+200C>ரில்லரும் மக்களை இந்தளவு கவர்ந்ததில்லை
+taf_01484_00774826591  சமீபத்தில் எந்த ஒரு த்ரில்லரும் மக்களை இந்தளவு கவர்ந்ததில்லை
 taf_01484_00831178429  வேண்டுமானால் எனது கிராமத்தில் வந்து கேட்டுப் பாருங்கள்
 taf_01484_00864867957  இந்தியக் கடற்படையினரின் தாக்குதலில் கடற்கொள்ளையர் இருபத்தி எட்டு பேர் சிக்கினர்
 taf_01484_00880662951  தென்மேற்குப் பருவமழை பொய்த்துவிட்டதால் காவிரியின் குறுக்கே உள்ள அணைகளில் நீரின் இருப்பு குறைவாக உள்ளது
 taf_01484_00883515123  குருவின் ஆதிக்கம் இருந்தால் அனைத்து தரப்பிலும் வெற்றி கிடைக்கும்
-taf_01484_00886973631  நட்சத்திரம் என்பது என்ன?
+taf_01484_00886973631  நட்சத்திரம் என்பது என்ன
 taf_01484_00968514257  புகழ்பெற்ற தர்காவுக்கு சென்று வரவும் அறிவுறுத்தினேன்
sk5057@speech-rec-vm:~/kaldi/egs/tamil_telugu_proj/s5_r3/db$ git diff 
FETCH_HEAD    HEAD          ORIG_HEAD     main          master        origin/main   
sk5057@speech-rec-vm:~/kaldi/egs/tamil_telugu_proj/s5_r3/db$ git diff 
FETCH_HEAD    HEAD          ORIG_HEAD     main          master        origin/main   
sk5057@speech-rec-vm:~/kaldi/egs/tamil_telugu_proj/s5_r3/db$ git diff --short-stat
error: invalid option: --short-stat
sk5057@speech-rec-vm:~/kaldi/egs/tamil_telugu_proj/s5_r3/db$ git diff --shortstat
 2 files changed, 128 insertions(+), 128 deletions(-)

```
### iitmasr kaldi db log
```
sk5057@speech-rec-vm:~/asr_project/git_repo/dataset_related$ python3 -u create_data_files.py | tee ../kaldi_tamtel_db/logs/ittmasr_proprocess_1.log 
2022-05-07 07:26:38.236915 Running on iitm_asr train
2022-05-07 07:26:38.237125 Processing /home/sk5057/kaldi/egs/tamil_telugu_proj/s5_r3/db/asriitm_tamil/train_transcription.txt for iitm_asr-train
2022-05-07 07:26:39.549060 pure_eng_lines_count: 24
2022-05-07 07:26:39.549117 comb_word_lines_count: 0
2022-05-07 07:26:39.549125 unclean_lines_count: 0
2022-05-07 07:26:39.549219 Writing text to /home/sk5057/kaldi/egs/tamil_telugu_proj/s5_r3/db/asriitm_tamil/transcription/train/text
2022-05-07 07:26:39.688353 Running on iitm_asr dev
2022-05-07 07:26:39.688582 Processing /home/sk5057/kaldi/egs/tamil_telugu_proj/s5_r3/db/asriitm_tamil/dev_transcription.txt for iitm_asr-dev
2022-05-07 07:26:39.742587 pure_eng_lines_count: 0
2022-05-07 07:26:39.742639 comb_word_lines_count: 0
2022-05-07 07:26:39.742646 unclean_lines_count: 0
2022-05-07 07:26:39.747655 Writing text to /home/sk5057/kaldi/egs/tamil_telugu_proj/s5_r3/db/asriitm_tamil/transcription/dev/text
2022-05-07 07:26:39.750841 Running on iitm_asr test
2022-05-07 07:26:39.751003 Processing /home/sk5057/kaldi/egs/tamil_telugu_proj/s5_r3/db/asriitm_tamil/test_transcription.txt for iitm_asr-test
2022-05-07 07:26:39.802771 pure_eng_lines_count: 1
2022-05-07 07:26:39.802822 comb_word_lines_count: 1
2022-05-07 07:26:39.802829 unclean_lines_count: 0
2022-05-07 07:26:39.803197 Writing text to /home/sk5057/kaldi/egs/tamil_telugu_proj/s5_r3/db/asriitm_tamil/transcription/test/text

```

### Created new repo for kaldi db as submodule
### Created new repo for kaldi recipe (modified tedlium) as submodule
Ran create_lexicon for new text after new preprocessing

```
sk5057@speech-rec-vm:~/kaldi/egs/tamil_telugu_proj/s5_r3/db$ mkdir ../data
sk5057@speech-rec-vm:~/kaldi/egs/tamil_telugu_proj/s5_r3/db$ cp -r combined_transcription/* ../data/
```



sk5057@speech-rec-vm:~/kaldi/egs/tedlium/s5_r3/db/TEDLIUM_release-3/LM$ gunzip -c *.en.gz | sed 's/ <\/s>//g' | gzip -c  > out/train.txt.gz



sk5057@speech-rec-vm:~/kaldi$ find . -name "validate_vocab.py" -print
./tools/pocolm/scripts/validate_vocab.py



def GetNumWords(lm_dir_in):
    command = "tail -n 1 {0}/words.txt".format(lm_dir_in)
    line = subprocess.check_output(command,
                                   shell=True,
                                   universal_newlines=True
                                   encoding='utf-8')

