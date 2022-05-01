#!/bin/bash
COUNTER=$(( 0 ))
for i in clips/*.mp3
do
    #sox -G -v 0.95 "$i" -r 16k -e signed-integer "wavclips/$(basename -s .mp3 "$i").wav"
    sox -G "$i" -r 16k -e signed-integer "wavclips/$(basename -s .mp3 "$i").wav"
    (( COUNTER++ ))
    if [ $(( $COUNTER % 1000 )) -eq 0 ] ; then
    	echo $COUNTER
        #echo "Your number is divisible by 5"
    fi
    #echo $COUNTER
    #break
done
