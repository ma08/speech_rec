#!/bin/bash
LANG=C
LANGUAGE=en_IN.utf8
LANG=en_IN.utf8


function echo_ts
{
	echo $1 | ts
}
#alias echo=echo_ts

#echo_ts "aaa"
#exit

echo_ts "STARTING STAGE 1"
./remove_parantheses.awk $1 > stage1_out_telugu.txt 2> errors.log
echo_ts "FINISHED STAGE 1"

echo_ts "STARTING STAGE 2"
./remove_urls.sh stage1_out_telugu.txt > stage2_out_telugu.txt 2> errors.log
echo_ts "FINISHED STAGE 2"

echo_ts "STARTING STAGE 3"
./replace_num_telugu.sh stage2_out_telugu.txt stage3_out_telugu.txt
echo_ts "FINISHED STAGE 3"

echo_ts "STARTING STAGE 4"
./remove_chars_tamil.sh stage3_out_telugu.txt > stage4_out_telugu.txt
echo_ts "FINISHED STAGE 4"

echo_ts "STARTING STAGE 5"
./fix_whitespace.sh stage4_out_telugu.txt > stage5_out_telugu.txt
echo_ts "FINISHED STAGE 5"

#After this merge original corpus with one from iitm
