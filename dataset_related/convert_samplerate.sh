#!/bin/bash
cd $1
COUNTER=$(( 0 ))
mkdir resampled_Audio
for i in Audio/*.wav
do
    sox -G "$i" -r 16k -e signed-integer "resampled_Audio/$(basename -s .wav "$i").wav"
    (( COUNTER++ ))
    if [ $(( $COUNTER % 1000 )) -eq 0 ] ; then
    	echo $COUNTER
        #echo "Your number is divisible by 5"
    fi
    #echo $COUNTER
    #break
done
