#! /usr/bin/env bash

echo "Count th words in spider.txt, then sort the words by frequency"
echo "Create new file spider_head_words"
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head > spider_head_words.txt
echo "Show content of the created file"
cat spider_head_words.txt
sleep 5
clear