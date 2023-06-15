#! /usr/bin/env bash

echo "Append output from a python program to a file"
./stdout_example.py >> new_file.txt
echo ""
echo "Show output appended in a file"
cat new_file.txt