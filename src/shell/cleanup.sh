#!/bin/bash

# Cleanup temporary files
echo "Cleaning up temporary files..."

find . -type f -name "*.tmp" -delete
find . -type f -name "*.log" -delete
find . -type d -name "__pycache__" -exec rm -rf {} +

echo "Cleanup complete."
