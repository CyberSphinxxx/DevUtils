import base64
import sys

def encode_text(text):
    """Encodes text to Base64."""
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    return encoded_bytes.decode("utf-8")

def decode_text(encoded_text):
    """Decodes Base64 text."""
    decoded_bytes = base64.b64decode(encoded_text)
    return decoded_bytes.decode("utf-8")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python base64_encoder.py <encode|decode> <text>")
    else:
        action = sys.argv[1].lower()
        text = sys.argv[2]
        if action == "encode":
            print(encode_text(text))
        elif action == "decode":
            print(decode_text(text))
        else:
            print("Invalid action. Use 'encode' or 'decode'.")
