#!/bin/bash

final_line=""
for word in $(cat story.txt); do
	B=$(echo -n "${word:0:1}" | tr "[:lower:]" "[:upper:]")
	final_line="${final_line}${B}${word:1:${#word}} "
done

echo $final_line

echo -e "\n"