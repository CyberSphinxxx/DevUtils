import uuid
import sys

def generate_uuid(version=4):
    """Generates a UUID."""
    if version == 1:
        return uuid.uuid1()
    elif version == 4:
        return uuid.uuid4()
    else:
        return "Unsupported UUID version"

if __name__ == "__main__":
    version = 4
    if len(sys.argv) > 1:
        try:
            version = int(sys.argv[1])
        except ValueError:
            pass
    
    print(f"UUID v{version}: {generate_uuid(version)}")
