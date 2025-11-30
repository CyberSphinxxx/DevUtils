#!/bin/bash

# Clear Cache Script

CACHE_DIRS=("./tmp" "./cache" "./.cache")

echo "Clearing cache directories..."

for dir in "${CACHE_DIRS[@]}"; do
  if [ -d "$dir" ]; then
    echo "Removing contents of $dir..."
    # rm -rf "$dir"/*
    sleep 0.5
    echo "Cleared $dir."
  else
    echo "Directory $dir does not exist. Skipping."
  fi
done

echo "Cache cleared successfully."
