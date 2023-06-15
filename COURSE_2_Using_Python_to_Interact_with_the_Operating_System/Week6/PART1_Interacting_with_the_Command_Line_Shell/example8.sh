#! /usr/bin/env bash

echo "Capitalize lines from a file"
echo "Alternative form"
echo ""
echo "Original content"
cat haiku.txt
echo ""
./capitalize.py < haiku.txt > new_haiku2.txt
echo ""
echo "Final Content"
cat new_haiku2.txt