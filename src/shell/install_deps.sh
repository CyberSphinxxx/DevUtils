#!/bin/bash

# Mock Dependency Installation Script

echo "Checking for 'package.json'..."
if [ -f "package.json" ]; then
    echo "Found package.json. Installing Node.js dependencies..."
    # npm install
    sleep 2
    echo "Node.js dependencies installed."
else
    echo "No package.json found."
fi

echo "Checking for 'requirements.txt'..."
if [ -f "requirements.txt" ]; then
    echo "Found requirements.txt. Installing Python dependencies..."
    # pip install -r requirements.txt
    sleep 2
    echo "Python dependencies installed."
else
    echo "No requirements.txt found."
fi

echo "All dependencies checked."
