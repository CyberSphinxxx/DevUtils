import sys
import os
# Note: Requires PyPDF2 installed
# pip install PyPDF2

def merge_pdfs(output_path, input_paths):
    """
    Merges multiple PDF files into one.
    """
    try:
        from PyPDF2 import PdfMerger
    except ImportError:
        print("PyPDF2 is not installed. Please install it using 'pip install PyPDF2'")
        return

    merger = PdfMerger()

    for path in input_paths:
        if os.path.exists(path):
            merger.append(path)
            print(f"Appended {path}")
        else:
            print(f"File not found: {path}")

    merger.write(output_path)
    merger.close()
    print(f"Successfully merged PDFs into {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pdf_merger.py <output_file.pdf> <input_file1.pdf> <input_file2.pdf> ...")
    else:
        merge_pdfs(sys.argv[1], sys.argv[2:])
