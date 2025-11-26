import csv
import json
import sys

def csv_to_json(csv_file_path, json_file_path):
    """Converts a CSV file to JSON."""
    data = []
    try:
        with open(csv_file_path, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(data, indent=4))
            
        print(f"Successfully converted {csv_file_path} to {json_file_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python csv_to_json.py <input_csv> <output_json>")
    else:
        csv_to_json(sys.argv[1], sys.argv[2])
