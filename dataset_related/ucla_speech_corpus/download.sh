#!/bin/bash
filename=$1
echo Start
while read p; do 
    wget "$p"
done < "$filename"