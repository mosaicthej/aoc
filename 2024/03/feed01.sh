#!/usr/bin/bash

# expecting 'cat input'
(sed 's/\(mul([0-9]\+,[0-9]\+)\)/\n\1\n/g' \
    | grep 'mul([0-9]\+,[0-9]\+)' \
    | sed 's/\mul(\([0-9]*\),\([0-9]*\))/\1*\2/' && echo '') \
    | ./adder.py 
