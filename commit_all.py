import subprocess
import os

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command {' '.join(command)}: {e.stderr}")
        return None

def main():
    # Stage all files first
    print("Staging all files...")
    run_command(['git', 'add', '.'])

    # Get status of staged files
    status_output = run_command(['git', 'status', '--porcelain'])
    if not status_output:
        print("No changes found.")
        return

    files_to_commit = []
    for line in status_output.split('\n'):
        if not line.strip():
            continue
        
        # Porcelain format: XY PATH
        # XY are status codes. PATH starts at index 3.
        # But let's be safer: find the first space after index 2?
        # Actually, standard porcelain is strictly index 3 for path start.
        # Let's try to just take the rest of the line.
        
        filename = line[3:].strip()
        
        # Handle renamed files if necessary (format: R  old -> new)
        if '->' in filename:
            filename = filename.split('->')[-1].strip()
            
        # Remove quotes if present
        if filename.startswith('"') and filename.endswith('"'):
            filename = filename[1:-1]
            
        files_to_commit.append(filename)

    print(f"Found {len(files_to_commit)} files to commit.")

    for filename in files_to_commit:
        print(f"Committing {filename}...")
        
        # Determine message
        # Since we don't track status per file easily here (all are staged 'A' or 'M'),
        # we'll just use a generic "Update" or "Add" based on file existence?
        # Or just "Add/Update <filename>"
        
        message = f"Add/Update {os.path.basename(filename)}"
            
        # Commit specific file
        # Note: git commit -m "msg" -- <file> commits the changes to that file from the index.
        run_command(['git', 'commit', '-m', message, '--', filename])

if __name__ == "__main__":
    main()
