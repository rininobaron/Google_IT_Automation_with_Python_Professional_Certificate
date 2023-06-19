#! /bin/bash

file=$0
len=${#file}
file=${file:2:len}

echo "Create dated copy from this script"
DATE=$(date +"%F")
new_file=$DATE"_"$file
echo $new_file
cp $file $new_file
ls $new_file