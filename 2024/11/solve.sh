#!/bin/bash

# Check if N is provided as a command-line argument
if [ -z "$1" ]; then
  echo "Usage: $0 <N>"
  exit 1
fi

# Read N from the command-line argument
N=$1

# Create a temporary file to store intermediate results
# temp_file=$(mktemp)
touch tempbuf

wd=$(dirname "$0")
# Read a line of numbers from stdin and save it to the temp file
cat $wd/input > "tempbuf"

# Loop N times
for ((i = 0; i < N; i++)); do
  # Process the file content with ./a.out and overwrite the temp file
  ./blink < "tempbuf" > "tempbuf1" && mv "tempbuf1" "tempbuf"
  echo "blink $i...."
done

# Print the final output
cat "tempbuf"

wc -w "tempbuf"
# Clean up the temporary file

