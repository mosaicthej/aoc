#!/bin/bash

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <input_directory> <output_directory>"
  exit 1
fi

INPUT_DIR=$1
OUTPUT_DIR=$2

if [[ ! -d $INPUT_DIR ]]; then
  echo "Error: Input directory does not exist."
  exit 1
fi

if [[ ! -d $OUTPUT_DIR ]]; then
  echo "Output directory does not exist. Creating it..."
  mkdir -p "$OUTPUT_DIR"
fi

for txt_file in "$INPUT_DIR"/*.txt; do
  if [[ -f $txt_file ]]; then
    echo "Processing $txt_file..."
    output_file="$OUTPUT_DIR/$(basename "${txt_file%.txt}.bmp")"
    ./writebitmap "$txt_file"
    mv "$(basename "${txt_file%.txt}.bmp")" "$output_file"
    echo "Saved $output_file"
  fi
done

