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
./remove_parantheses.awk $1 > stage1_out.txt 2> errors.log
echo_ts "FINISHED STAGE 1"

echo_ts "STARTING STAGE 2"
./remove_urls.sh stage1_out.txt > stage2_out.txt 2> errors.log
echo_ts "FINISHED STAGE 2"

echo_ts "STARTING STAGE 3"
./replace_num.sh stage2_out.txt stage3_out.txt
echo_ts "FINISHED STAGE 3"

echo_ts "STARTING STAGE 4"
./remove_chars.sh stage3_out.txt > stage4_out.txt
echo_ts "FINISHED STAGE 4"

echo_ts "STARTING STAGE 5"
./fix_whitespace.sh stage4_out.txt > stage5_out.txt
echo_ts "FINISHED STAGE 5"
