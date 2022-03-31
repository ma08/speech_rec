#!/usr/bin/gawk -f
#Remove parantheses and all kinds of brackets with text in them
{
    gsub(/\(.*\)/,"")
    gsub(/\[.*\]/,"")
    gsub(/<.*>/,"")
    gsub(/{.*}/,"")
    print
}



