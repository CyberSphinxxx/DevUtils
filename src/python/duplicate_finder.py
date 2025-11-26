import hashlib
import os
import sys

def find_duplicates(directory):
    """
    Finds duplicate files in a directory based on MD5 hash.
    """
    hashes = {}
    duplicates = []

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                
                if file_hash in hashes:
                    duplicates.append((filepath, hashes[file_hash]))
                else:
                    hashes[file_hash] = filepath
            except OSError:
                continue

    if duplicates:
        print("Found duplicates:")
        for dup in duplicates:
            print(f"{dup[0]} is a duplicate of {dup[1]}")
    else:
        print("No duplicates found.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        find_duplicates(sys.argv[1])
    else:
        print("Usage: python duplicate_finder.py <directory>")
