sk5057@speech-rec-vm:~/dataset/microsoftspeechcorpusindianlanguages/ta-in-Train/Audios$ soxi 001990001.wav 

Input File     : '001990001.wav'
Channels       : 1
Sample Rate    : 16000
Precision      : 16-bit
Duration       : 00:00:04.64 = 74240 samples ~ 348 CDDA sectors
File Size      : 149k
Bit Rate       : 256k
Sample Encoding: 16-bit Signed Integer PCM


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


sk5057@speech-rec-vm:~/dataset/cv-corpus-8.0-2022-01-19/ta/clips$ ls -l | wc -l
197734


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


