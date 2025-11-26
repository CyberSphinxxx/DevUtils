import json
import csv
import sys
import os

def json_to_csv(json_file, csv_file):
    """
    Converts a JSON file to a CSV file.
    Assumes the JSON is a list of dictionaries.
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        if not isinstance(data, list):
            print("Error: JSON data must be a list of objects.")
            return

        if not data:
            print("Error: JSON data is empty.")
            return

        headers = data[0].keys()

        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Successfully converted {json_file} to {csv_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python json_to_csv.py <input_json> <output_csv>")
    else:
        json_to_csv(sys.argv[1], sys.argv[2])
