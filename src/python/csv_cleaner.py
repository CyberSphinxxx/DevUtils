import csv
import argparse
import os

def clean_csv(input_file, output_file):
    """
    Cleans a CSV file by removing empty rows and stripping whitespace from cells.
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
             open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            
            row_count = 0
            for row in reader:
                # Remove empty rows
                if not any(row):
                    continue
                
                # Strip whitespace from each cell
                cleaned_row = [cell.strip() for cell in row]
                writer.writerow(cleaned_row)
                row_count += 1
                
        print(f"Successfully cleaned CSV. Processed {row_count} rows.")
        print(f"Output saved to '{output_file}'.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean and normalize CSV data.")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to the output CSV file")
    
    args = parser.parse_args()
    
    clean_csv(args.input_file, args.output_file)
