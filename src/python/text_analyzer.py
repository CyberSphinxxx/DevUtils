import sys

def analyze_text(file_path):
    """Analyzes a text file for word count, char count, and line count."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        lines = text.splitlines()
        words = text.split()
        chars = len(text)
        
        print(f"Analysis for {file_path}:")
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {chars}")
        
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python text_analyzer.py <file_path>")
    else:
        analyze_text(sys.argv[1])
