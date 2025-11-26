import os
import shutil
from pathlib import Path

def organize_files(directory):
    """
    Organizes files in the specified directory into subdirectories based on their file extensions.
    """
    path = Path(directory)
    if not path.exists():
        print(f"Directory {directory} does not exist.")
        return

    for file_path in path.iterdir():
        if file_path.is_file():
            extension = file_path.suffix.lower()
            if extension:
                # Remove the dot from the extension
                folder_name = extension[1:]
                folder_path = path / folder_name
                
                folder_path.mkdir(exist_ok=True)
                
                destination = folder_path / file_path.name
                shutil.move(str(file_path), str(destination))
                print(f"Moved {file_path.name} to {folder_name}/")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
        organize_files(target_dir)
    else:
        print("Usage: python file_organizer.py <directory_path>")
