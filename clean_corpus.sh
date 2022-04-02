#!/bin/bash
LANG=C
LANGUAGE=en_IN.utf8
LANG=en_IN.utf8

echo "STARTING STAGE 1"
./remove_parantheses.awk $1 > stage1_out.txt
echo "FINISHED STAGE 1"
echo "STARTING STAGE 2"
./remove_urls.sh stage1_out.txt > stage2_out.txt
echo "FINISHED STAGE 2"
echo "STARTING STAGE 3"
perl replace_num.pl < stage2_out.txt > stage3_out.txt
echo "FINISHED STAGE 3"
# echo "STARTING STAGE 4"
# ./remove_urls.sh stage3_out.txt > stage4_out.txt
# echo "FINISHED STAGE 4"