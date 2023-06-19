#! /bin/bash

DIR='/usr/share/dict/words'

number=$1

echo "Select a random word"
echo "from $DIR"
if test $number > 0; then
	number=$1
	egrep "^[A-Za-z]{$number}$" $DIR | sort -R | head -n 1
else
	sort -R $DIR | head -n 1
fi