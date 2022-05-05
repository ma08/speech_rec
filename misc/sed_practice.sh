sed -E 's/([0-9]+)/NUM/g' test_num.txt 

echo "-------"

sed -E 's/([0-9]+)/echo "NUM\1"/g' test_num.txt 

sed -E 's/([0-9]+)/python3 indic-num2words/num_to_word.py "\1"/g' test_num.txt 


sed -E -e 's/([0-9]+)/'"`python3 indic-num2words/num_to_word.py \1 ta`"'/g' tamil/sample_top50000_lines.txt > num_out.txt

