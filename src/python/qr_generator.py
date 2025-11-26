import sys
# Note: Requires qrcode installed
# pip install qrcode[pil]

def generate_qr(data, output_file="qrcode.png"):
    """
    Generates a QR code for the given data.
    """
    try:
        import qrcode
    except ImportError:
        print("qrcode library is not installed. Please install it using 'pip install qrcode[pil]'")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"QR code generated and saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python qr_generator.py <data> [output_file]")
    else:
        data = sys.argv[1]
        output = sys.argv[2] if len(sys.argv) > 2 else "qrcode.png"
        generate_qr(data, output)
