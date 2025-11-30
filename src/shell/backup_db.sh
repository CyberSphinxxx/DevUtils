#!/bin/bash

# Mock Database Backup Script
# Usage: ./backup_db.sh [db_name]

DB_NAME=$1
BACKUP_DIR="./backups"
DATE=$(date +%Y%m%d_%H%M%S)

if [ -z "$DB_NAME" ]; then
  echo "Usage: $0 <database_name>"
  exit 1
fi

echo "Starting backup for database: $DB_NAME"
echo "Backup directory: $BACKUP_DIR"

# Simulate backup process
mkdir -p "$BACKUP_DIR"
echo "Dumping data..."
sleep 2

BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_$DATE.sql"
touch "$BACKUP_FILE"

echo "Backup completed successfully."
echo "Backup file created: $BACKUP_FILE"
