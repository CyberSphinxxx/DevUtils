import argparse
import os
import sys

def resize_image(input_file, output_file, width, height):
    """
    Mock function to resize an image. 
    In a real scenario, this would use PIL/Pillow.
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    print(f"Processing '{input_file}'...")
    print(f"Resizing to {width}x{height}...")
    
    # Simulate processing time
    import time
    time.sleep(0.5)
    
    # Just copy the file for this mock
    try:
        with open(input_file, 'rb') as src, open(output_file, 'wb') as dst:
            dst.write(src.read())
        print(f"Success: Image saved to '{output_file}' (Mock resized).")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize images (Mock).")
    parser.add_argument("input_file", help="Path to the input image")
    parser.add_argument("output_file", help="Path to the output image")
    parser.add_argument("-w", "--width", type=int, required=True, help="Target width")
    parser.add_argument("-H", "--height", type=int, required=True, help="Target height")
    
    args = parser.parse_args()
    
    resize_image(args.input_file, args.output_file, args.width, args.height)
