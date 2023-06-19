#! /bin/bash

if [ -x $1 ]; then
	echo "It's executable"
else
	echo "It's NOT executable"
fi

if [ -w $1 ]; then
	echo "It's writable"
else
	echo "It's NOT writable"
fi