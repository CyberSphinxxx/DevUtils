#!/bin/bash

# Disk Usage Check Script

THRESHOLD=90

echo "Checking disk usage..."

df -H | grep -vE '^Filesystem|tmpfs|cdrom' | awk '{ print $5 " " $1 }' | while read output;
do
  usep=$(echo $output | awk '{ print $1}' | cut -d'%' -f1  )
  partition=$(echo $output | awk '{ print $2 }' )
  
  if [ $usep -ge $THRESHOLD ]; then
    echo "WARNING: Partition \"$partition\" has used $usep% of available space."
  else
    echo "OK: Partition \"$partition\" is at $usep% usage."
  fi
done
