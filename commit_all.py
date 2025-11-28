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
    # Get status
    status_output = run_command(['git', 'status', '--porcelain'])
    if not status_output:
        print("No changes found.")
        return

    files_to_commit = []
    for line in status_output.split('\n'):
        if not line.strip():
            continue
        
        # Status is first 2 chars, filename follows
        status = line[:2]
        filename = line[3:].strip()
        
        # Handle renamed files if necessary (format: R  old -> new)
        if '->' in filename:
            filename = filename.split('->')[-1].strip()
            
        # Remove quotes if present
        if filename.startswith('"') and filename.endswith('"'):
            filename = filename[1:-1]
            
        files_to_commit.append((status, filename))

    print(f"Found {len(files_to_commit)} files to commit.")

    for status, filename in files_to_commit:
        print(f"Processing {filename}...")
        
        # Add file
        run_command(['git', 'add', filename])
        
        # Determine message
        if '??' in status:
            message = f"Add {os.path.basename(filename)}"
        else:
            message = f"Update {os.path.basename(filename)}"
            
        # Commit
        run_command(['git', 'commit', '-m', message])
        print(f"Committed {filename}")

if __name__ == "__main__":
    main()
