#!/usr/bin/gawk -f
#Remove parantheses and all kinds of brackets with text in them
# {
#     gsub(/\(.*\)/,"")
#     gsub(/\[.*\]/,"")
#     gsub(/<.*>/,"")
#     gsub(/{.*}/,"")
#     print
# }
    #  cmd = "python3 indic-num2words/num_to_word.py "




    # gsub(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z\uB02-\uBCD0-9@:%_\+.~#?&//=]*)/, "")
    # gsub(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}[\<\>]([-a-zA-Z\xB02-\xBCD0-9@:%_\+.~#?&//=]*)/, "")
    # gsub(/[-a-zA-Z0-9@:%_\+.~#?&\/\/=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&\/\/=]*)?/,"")
# {
#     /[0-9][,0-9]*/
#     print
# }
# // {print $0}


# gsub(/([0-9]+)/, system("echo number &"))



#WORKING!
# gsub(/([0-9]+)/, "number: &")


# /([0-9][0-9]*)/ {
#     # var="\\\\&";
#     print $&
#     # system(")
#     # cmd="echo -ne \"$2"\" | echo \"$2""\""
#     # if ( (cmd | getline x) > 0 ) {
#     #     $2 = x
#     # }
#     # close(cmd)
# }{print ""}

# /([0-9][0-9]*)/ 

#WORKING! but only single match in a while
{match($0, /([0-9][0-9]*)/, group); print group[0]}{print ""}


# {print "foo"}
# https://regexr.com/3e6m0



