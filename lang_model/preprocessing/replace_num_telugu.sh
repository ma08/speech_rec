#!/bin/bash
sed -E -e 's/([0-9]+)/'"`python3 indic-num2words/num_to_word.py \1 te`"'/g' $1 > $2
