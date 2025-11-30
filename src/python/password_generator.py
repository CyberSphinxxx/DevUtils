import secrets
import string
import argparse

def generate_password(length=12, include_symbols=True):
    """
    Generates a secure random password.
    """
    if length < 4:
        print("Error: Password length must be at least 4.")
        return None

    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols from the password")
    
    args = parser.parse_args()
    
    password = generate_password(args.length, not args.no_symbols)
    if password:
        print(f"Generated Password: {password}")
