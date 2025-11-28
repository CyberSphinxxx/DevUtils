#!/bin/bash

# Monitor script
# Usage: ./monitor.sh

echo "System Status:"
echo "----------------"
echo "Date: $(date)"
echo "Uptime: $(uptime -p)"
echo "----------------"
echo "Memory Usage:"
free -h
echo "----------------"
echo "Disk Usage:"
df -h /
