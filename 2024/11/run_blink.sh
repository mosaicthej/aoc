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

# Initialize the total sum
total_sum=0

# Create temporary files
temp_file=$(mktemp)
temp_result=$(mktemp)

# Loop through each number in the input
for num in $line; do
  # Write the number to the temp file
  echo "$num" > "$temp_file"
  
  # Process the number N times
  for ((i = 0; i < N; i++)); do
    ./blink < "$temp_file" > "$temp_result" && mv "$temp_result" "$temp_file"
    echo "blink $i th... on $num...."
  done

  # Read the final result and add it to the total sum
  result=$(cat "$temp_file" | wc -w)
  total_sum=$((total_sum + result))
done

# Output the final total sum
echo "$total_sum"

# Clean up temporary files
rm -f "$temp_file" "$temp_result"

