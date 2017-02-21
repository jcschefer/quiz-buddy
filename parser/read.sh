#!/usr/bin/zsh
cd "$(/home/rz5000/name_pending/parser/www.quizbowlpackets.com "$0")"
echo $(ls)
for file in $(ls)
	do
	cat "$file";
	done
