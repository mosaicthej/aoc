#!/usr/bin/bash

# expecting 'cat input'

# make a remover from lex
flex -t remover.lex | clang -x c - -o remover -lfl

# clean it and run through part1's script
tr -d '\n' | ./remover | ./feed01.sh
