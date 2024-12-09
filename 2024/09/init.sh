#!/usr/bin/sh
# run through the input file,
# count the number of lines, 
# and return num lines as well as inputs

wd=$(dirname "$0")
n=$(wc $wd/input -l  | awk '{ print $1 }')
m=$(head -n 1 $wd/input | wc -c)
m=$(( $m-1 ))
echo $n $m
cat $wd/input


