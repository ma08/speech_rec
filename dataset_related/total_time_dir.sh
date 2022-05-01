#!/bin/bash
shopt -s extglob
if [[ "$#" -lt 1 ]]; then
	echo "find files!"
	echo "  sox_duration_total *.wav"
	echo ""
	return
fi
names=( $@ )
#echo "------"
input_dir=$(realpath $1)
#echo "$input_dir"
#echo "$@"
#pwd
#echo $names
input_dir="$1"
#FILES=("$input_dir"/*.wav)
#echo "${FILES[@]}"
#echo "------"
COUNTER=$(( 0 ))
#for i in "${names[@]}"; do
for i in "$input_dir"/*.wav; do
#for i in "$@"; do
#	echo "!!!!!!!!!!!"
#	echo "$i"
#	echo "!!!!!!!!!!!"
	val=`soxi -d "$i"`
	(( COUNTER++ ))
	if [ $(( $COUNTER % 1000 )) -eq 0 ] ; then
		echo "$COUNTER done so far"
		#echo "Your number is divisible by 5"
	fi
	# echo "$val | $i"
done
echo "Total $COUNTER files"
soxi -D "$@" | python3 -c "import sys;print(\"\ntotal sec:    \" +str( sum(float(l) for l in sys.stdin)))"
soxi -D "$@" | python3 -c "import sys;print(\"total minutes:    \" +str( sum(float(l) for l in sys.stdin)/60 ))"
soxi -D "$@" | python3 -c "import sys;print(\"\nmin sec:    \" +str( min(float(l) for l in sys.stdin)))"
soxi -D "$@" | python3 -c "import sys;print(\"\nmax sec:    \" +str( max(float(l) for l in sys.stdin)))"
soxi -D "$@" | python3 -c "import sys;import datetime;print(\"running time: \" +str( datetime.timedelta(seconds=sum(float(l) for l in sys.stdin)) ))"
