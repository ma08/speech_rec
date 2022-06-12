db_folder=~/kaldi/egs/tamil_telugu_proj/s5_r3/db
proj_root_folder=~/kaldi/egs/tamil_telugu_proj/s5_r3/
# for dataset in microsoft_tamil  mozillacv_tamil  openslr_tamil; do
for dataset in openslr_tamil; do
    for parition in dev train test; do
        echo "running on $dataset $parition"
        dir=$db_folder/$dataset/transcription/$parition
        cat $dir/utt2spk | $proj_root_folder/utils/utt2spk_to_spk2utt.pl > $dir/spk2utt
    done
done


