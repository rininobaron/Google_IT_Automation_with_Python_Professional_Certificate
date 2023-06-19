#! /bin/bash

DIR='/usr/share/dict/words'

echo "Select a random word"
echo "from $DIR"
sort -R $DIR | head -n 1