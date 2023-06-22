#!/bin/bash

files=$(grep " jane " ../data/list.txt | cut -d' ' -f3)

for file in $files; do
	if test -e ${HOME}${file}; then
		echo ${HOME}${file} >> oldFiles.txt
	fi
done

cat oldFiles.txt