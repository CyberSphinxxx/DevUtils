#!/bin/bash

# Cleanup script
# Usage: ./cleanup.sh <directory>

TARGET_DIR=$1

if [ -z "$TARGET_DIR" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Directory does not exist."
    exit 1
fi

echo "Cleaning up temporary files in $TARGET_DIR..."
find "$TARGET_DIR" -name "*.tmp" -type f -delete
find "$TARGET_DIR" -name "*.log" -type f -delete
find "$TARGET_DIR" -name ".DS_Store" -type f -delete

echo "Cleanup complete."
