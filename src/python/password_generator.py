import random
import string
import sys

def generate_password(length=12, use_special_chars=True):
    """
    Generates a secure random password.
    """
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    length = 12
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
        except ValueError:
            print("Invalid length. Using default 12.")
    
    print(f"Generated Password: {generate_password(length)}")
