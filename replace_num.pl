#!/usr/bin/perl
while (my $line = <>){
    while ($line =~ m/([0-9][0-9]*)/g)
    {
        my $num_in_word = qx{python3 indic-num2words/num_to_word.py $1 'ta'};
        chomp $num_in_word;
        $line =~ s/([0-9][0-9]*)/$num_in_word/;
    }
    print $line;
}
