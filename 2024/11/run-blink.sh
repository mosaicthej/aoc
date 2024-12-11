#!/bin/bash

# Check if N is provided as a command-line argument
if [ -z "$1" ]; then
  echo "Usage: $0 <N>"
  exit 1
fi

# Read N from the command-line argument
N=$1

# Create a temporary file to store intermediate results
temp_file=$(mktemp)

wd=$(dirname "$0")
# Read a line of numbers from stdin and save it to the temp file
#cat $wd/input > "$temp_file"
cat > "$temp_file"
#
# Loop N times
for ((i = 0; i < N; i++)); do
  # Process the file content with ./a.out and overwrite the temp file
  echo "working on blink $i..."
  ./blink < "$temp_file" > "$temp_file.tmp" && mv "$temp_file.tmp" "$temp_file"
done

# Print the final output
# cat "$temp_file"
# Print the final output
wc -w "$temp_file"
# Clean up the temporary file

