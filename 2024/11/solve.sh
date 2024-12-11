#!/bin/bash

# Check if N is provided as a command-line argument
if [ -z "$1" ]; then
  echo "Usage: $0 <N>"
  exit 1
fi

# Read N from the command-line argument
N=$1

# Read a line of numbers from stdin
read -r line

# Initialize the input for ./a.out with the input from stdin
input="$line"

# Loop N times
for ((i = 0; i < N; i++)); do
  # Feed the input to ./a.out and capture the output
  input=$(echo "$input" | ./a.out)
done

# Print the final output
echo "$input"
echo "$input" | wc -w

