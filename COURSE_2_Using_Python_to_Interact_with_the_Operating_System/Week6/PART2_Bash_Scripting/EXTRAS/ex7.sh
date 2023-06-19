#! /bin/bash

files=$@

echo "Create dated copy from passed files"
DATE=$(date +"%F")
for file in $files;
do
	file2=$(basename $file .sh)
	new_file=$file2"_"$DATE".sh"
	echo $new_file
	cp $file $new_file
done

ls