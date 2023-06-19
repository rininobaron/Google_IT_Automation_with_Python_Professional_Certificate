#! /bin/bash

file=$0
len=${#file}
file=${file:2:len}
file=$(basename $file .sh)
echo $file

echo "Create dated copy from this script"
DATE=$(date +"%F")
new_file=$file"_"$DATE".sh"
echo $new_file
file=$0
len=${#file}
file=${file:2:len}
cp $file $new_file
ls $new_file