#!/usr/bin/zsh
for file in $(ls ./)
do
	#cat test/$file > /dev/null
	#cat test/$file
    pdftotext ./$file
done
