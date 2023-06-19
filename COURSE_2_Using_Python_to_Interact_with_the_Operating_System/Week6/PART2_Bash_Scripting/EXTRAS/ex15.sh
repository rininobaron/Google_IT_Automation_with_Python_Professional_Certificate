#! /bin/bash

upper_limit=$2+1
lower_limit=$1
number=$(($RANDOM%upper_limit))
if [ $number -lt $lower_limit ]; then 
	echo $lower_limit
else
	echo $number
fi