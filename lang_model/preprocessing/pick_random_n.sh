#https://stackoverflow.com/a/10120570/3465519
perl -MList::Util=shuffle -e '$n = 25000; @foo = shuffle <>; print @foo[0..$n]' $1
