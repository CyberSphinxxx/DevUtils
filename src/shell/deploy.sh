#!/bin/bash

# Deploy script
# Usage: ./deploy.sh <environment>

ENV=$1

if [ -z "$ENV" ]; then
    echo "Usage: $0 <environment>"
    exit 1
fi

echo "Deploying to $ENV..."

# Simulate deployment steps
echo "1. Pulling latest code..."
sleep 1
echo "2. Installing dependencies..."
sleep 1
echo "3. Building application..."
sleep 1
echo "4. Restarting services..."
sleep 1

echo "Deployment to $ENV successful!"
