#! /bin/bash

let a=$1\*$2
echo $a
expr $1 \* $2
a=$(($1*$2))
echo $a