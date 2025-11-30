import json
import argparse
import os

def validate_json(input_file):
    """
    Validates if a file contains valid JSON.
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return False

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            json.load(f)
        print(f"Success: '{input_file}' contains valid JSON.")
        return True
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{input_file}'.")
        print(f"Details: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate JSON files.")
    parser.add_argument("input_file", help="Path to the JSON file to validate")
    
    args = parser.parse_args()
    
    validate_json(args.input_file)
