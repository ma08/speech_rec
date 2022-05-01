function sox_duration_total
{
  if [[ "$#" -lt 1 ]]; then
    echo "find files!"
    echo "  sox_duration_total *.wav"
    echo ""
    return
  fi
  for i in "$@"; do
    val=`soxi -d "$i"`
    # echo "$val | $i"
  done
  soxi -D "$@" | python3 -c "import sys;print(\"\ntotal sec:    \" +str( sum(float(l) for l in sys.stdin)))"
  soxi -D "$@" | python3 -c "import sys;print(\"total minutes:    \" +str( sum(float(l) for l in sys.stdin)/60 ))"
  soxi -D "$@" | python3 -c "import sys;print(\"\nmin sec:    \" +str( min(float(l) for l in sys.stdin)))"
  soxi -D "$@" | python3 -c "import sys;print(\"\nmax sec:    \" +str( max(float(l) for l in sys.stdin)))"
  soxi -D "$@" | python3 -c "import sys;import datetime;print(\"running time: \" +str( datetime.timedelta(seconds=sum(float(l) for l in sys.stdin)) ))"
}
#USage sox_duration_total path_to_dir/*.wav

sox_duration_total "$1"
