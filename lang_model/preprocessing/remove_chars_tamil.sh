# CHARS=$(python -c 'print u"“”‘’‚◯·—–•…″".encode("utf8")')
# sed 's/['"$CHARS"']//g' < stage3_after_tr_punc_remove.txt > stage3_remove_chars_out.txt
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# tr -d '[:punct:]' < stage3_out.txt > stage3_after_tr_punc_remove.txt
# sed 's/[^\xb80-\xbff]//g' < $1 
# sed 's/[^\xb80-\xbff\s\.]//g' < $1 

#U+00A0 : NO-BREAK SPACE [NBSP]
#U+0020 : SPACE [SP]

perl -CS -pe 's/[^\x{0B80}-\x{0BFF}\s\.]+//g' < $1

# perl -CSDA -plE 's/[\s\x{00A0}\x{0020}]+/ /g' $1 | tr . '\n' < $1 | sed -E '/^\s*$/d;s/^[ \t]*//;s/[ \t]*$//;s/[ \t]+/ /g;/^[[:space:]]*$/d' 
# perl -CSDA -plE 's/[\s\x{00A0}\x{0020}]+/ /g' $1 | tr . '\n' | sed -E 's/^[ \t]*//;s/[ \t]*$//;/^[[:space:]]*$/d' 
#perl -CSDA -plE 's/[\s\x{00A0}\x{0020}]+/ /g' $1 | tr . '\n' | sed -E 's/^[ \t]*//;s/[ \t]*$//;/^[[:space:]]*$/d' | grep -E "\s{1,}"

#https://stackoverflow.com/a/48163155/3465519
