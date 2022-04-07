sed -E 's/([0-9]+)/NUM/g' test_num.txt 

echo "-------"

sed -E 's/([0-9]+)/echo "NUM\1"/g' test_num.txt 
