#! /usr/bin/env bash

echo "Redirect the error output to new file"
./streams_err.py < new_file.txt 2> error_file.txt
echo ""
echo "Show output erroe saved in the target file"
cat error_file.txt
echo ""
sleep 3
echo "Execute again and Append new error in the target file"
./streams_err.py < new_file.txt 2>> error_file.txt
echo ""
echo "Show the appended error"
cat error_file.txt