#! /bin/bash

if [ -d $1 ]; then
	files=$(ls $1)
	counter=0
	for file in $files
	do
		if [ -e $file ]; then
			((counter++))
		fi
	done
	echo "Total files: "$counter
elif [ -e $1 ]; then
	size=$(ls -l $1 | awk '{ print $5 }')
	echo $size" bytes"
fi