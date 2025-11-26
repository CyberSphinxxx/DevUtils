from PIL import Image
import os
import sys

def resize_images(directory, width, height):
    """
    Resizes all images in a directory to the specified width and height.
    """
    if not os.path.exists(directory):
        print(f"Directory {directory} not found.")
        return

    output_dir = os.path.join(directory, "resized")
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            filepath = os.path.join(directory, filename)
            try:
                with Image.open(filepath) as img:
                    resized_img = img.resize((width, height))
                    output_path = os.path.join(output_dir, filename)
                    resized_img.save(output_path)
                    print(f"Resized {filename}")
            except Exception as e:
                print(f"Error resizing {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python image_resizer.py <directory> <width> <height>")
    else:
        resize_images(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
