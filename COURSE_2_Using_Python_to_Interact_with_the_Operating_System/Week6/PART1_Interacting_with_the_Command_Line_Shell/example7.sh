#! /usr/bin/env bash

echo "Capitalize lines from a file"
echo ""
echo "Original content"
cat haiku.txt
cat haiku.txt | ./capitalize.py > new_haiku.txt
echo ""
echo ""
echo "Final Content"
cat new_haiku.txt
sleep 5
clear