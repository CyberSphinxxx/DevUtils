#!/bin/bash

# Setup Environment script
# Usage: ./setup_env.sh

echo "Setting up development environment..."

# Check for required tools
TOOLS=("git" "node" "python3")

for tool in "${TOOLS[@]}"; do
    if ! command -v "$tool" &> /dev/null; then
        echo "Error: $tool is not installed."
    else
        echo "$tool is installed."
    fi
done

echo "Environment setup complete."
