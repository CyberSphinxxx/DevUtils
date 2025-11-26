#!/bin/bash

# Mock system monitor
echo "Monitoring system resources..."

while true; do
  echo "CPU: $(($RANDOM % 100))% | Memory: $(($RANDOM % 100))%"
  sleep 2
done
