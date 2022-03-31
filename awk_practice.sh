#!/bin/bash

#$0: current input line
# awk '/\(.*\)/{i++; print "\n"$0"\n"}' $1

# awk 'sub(/\(.*\)/,""){i++; print \n$0\n}' $1

# awk 'gsub(/\(.*\)/,""){i++;print "\n"$0"\n"} END{print i}' $1
# awk 'gsub(/\[.*\]/,""){i++;print "\n"$0"\n"} END{print i}' $1
# awk 'gsub(/\<.*\>/,""){i++;print "\n"$0"\n"} END{print i}' $1
# awk 'gsub(/\{.*\}/,""){i++;print "\n"$0"\n"} END{print i}' $1

#First match
# awk 'sub(/\(.*\)/,""){ print $0}' $1
# awk 'sub(/\[.*\]/,""){ print $0}' $1
# awk 'sub(/\<.*\>/,""){ print $0}' $1
# awk 'sub(/\{.*\}/,""){ print $0}' $1

#ALl matches
# awk '{print gsub(/\[.*\]/,"")}' $1


# awk '/\(.*\)/{i++;} END{print i}' $1
# awk '/\(.*\)/{i++;print "\n"$0"\n"} END {print i}' $1
# awk '/\[.*\]/{i++;print "\n"$0"\n"} END{print i}' $1
# awk '/\{.*\}/{i++;print "\n"$0"\n"} END{print i}' $1


# awk '/\<.*\>/{i++;print "\n"$0"\n"} END{print i}' $1
# awk '/\(.*\)/{i++;} END{print i " lines out of " NR}' $1

# awk '/[(¦)]/{i++; print $0}' $1



# gsub(/\(.*\)/,"")
# gsub(/\[.*\]/,"")
# /<.*>/
# gsub(/<.*>/,"")
# /{.*}/
# gsub(/{.*}/,"")
# /.*/

# gsub(/\(.*\)/ || /\[.*\]/ || /<.*>/ || /{.*}/,"")
# /(.*)/ #won't work, have to escape
# gsub(/\(.*\)/,""){print "\n"$0"\n"}
# /\[.*\]/
# gsub(/<.*>/,"")
# /\<.*\>/ #gives weird output, TODO: why?
# gsub(/\{.*\}/,"")



# {gsub(/\(.*\)/ || /\[.*\]/ || /<.*>/ || /{.*}/,"", $0); print}
# {gensub(/\(.*\)/ || /\[.*\]/ || /<.*>/ || /{.*}/,"", $0); print}
# /\(.*\)/ || /\[.*\]/ || /<.*>/ || /{.*}/
# /\(.*\)/ || /\[.*\]/ || /<.*>/ || /{.*}/ {print $0}