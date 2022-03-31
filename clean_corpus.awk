#!/usr/bin/gawk -f
#Remove parantheses and all kinds of brackets with text in them
# {
#     gsub(/\(.*\)/,"")
#     gsub(/\[.*\]/,"")
#     gsub(/<.*>/,"")
#     gsub(/{.*}/,"")
#     print
# }
{
    # gsub(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z\uB02-\uBCD0-9@:%_\+.~#?&//=]*)/, "")
    # gsub(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}[\<\>]([-a-zA-Z\xB02-\xBCD0-9@:%_\+.~#?&//=]*)/, "")
    gsub(/[-a-zA-Z0-9@:%_\+.~#?&\/\/=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&\/\/=]*)?/,"")
    print
}

# https://regexr.com/3e6m0



