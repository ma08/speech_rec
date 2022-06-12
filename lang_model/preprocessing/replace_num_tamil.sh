#!/bin/bash
sed -E -e 's/([0-9]+)/'"`python3 indic-num2words/num_to_word.py \1 ta`"'/g' $1 > $2
