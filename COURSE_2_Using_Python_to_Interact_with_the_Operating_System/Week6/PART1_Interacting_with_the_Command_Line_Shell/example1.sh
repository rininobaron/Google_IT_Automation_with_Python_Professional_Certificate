#! /usr/bin/env bash

echo "Save output from a python program to a file"
./stdout_example.py > new_file.txt
echo ""
echo "Show output in new file"
cat new_file.txt