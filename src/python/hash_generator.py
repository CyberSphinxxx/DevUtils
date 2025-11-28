import hashlib

def generate_hash(text, algorithm='sha256'):
    """
    Generates a hash for the given text using the specified algorithm.
    """
    if algorithm == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(text.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(text.encode()).hexdigest()
    else:
        return "Unsupported algorithm"

if __name__ == "__main__":
    text = "Hello, World!"
    print(f"Text: {text}")
    print(f"MD5: {generate_hash(text, 'md5')}")
    print(f"SHA1: {generate_hash(text, 'sha1')}")
    print(f"SHA256: {generate_hash(text, 'sha256')}")
