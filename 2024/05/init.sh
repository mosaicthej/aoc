#!/usr/bin/sh
# run through the input file,
# count the number of lines, 
# and return num lines as well as inputs

wd=$(dirname "$0")

nrules=$(grep '|' input | wc -l)
nprints=$(grep ',' input | wc -l)

echo $nrules; head -n $nrules $wd/input
echo $nprints; tail -n $nprints $wd/input
