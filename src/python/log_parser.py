import argparse
import os
import re
from collections import Counter

def analyze_logs(log_file):
    """
    Analyzes a log file for common patterns (ERROR, WARNING, INFO).
    """
    if not os.path.exists(log_file):
        print(f"Error: Log file '{log_file}' not found.")
        return

    log_levels = Counter()
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                if "ERROR" in line:
                    log_levels["ERROR"] += 1
                elif "WARNING" in line:
                    log_levels["WARNING"] += 1
                elif "INFO" in line:
                    log_levels["INFO"] += 1
                elif "DEBUG" in line:
                    log_levels["DEBUG"] += 1
                    
        print(f"Log Analysis Report for '{log_file}':")
        print("-" * 30)
        for level, count in log_levels.items():
            print(f"{level}: {count}")
        print("-" * 30)
        print(f"Total lines processed: {sum(log_levels.values())} (matching known levels)")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze log files.")
    parser.add_argument("log_file", help="Path to the log file")
    
    args = parser.parse_args()
    
    analyze_logs(args.log_file)
