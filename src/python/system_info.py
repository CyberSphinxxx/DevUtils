import platform
import sys

def get_system_info():
    """
    Prints basic system information.
    """
    info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": sys.version
    }

    print("System Information:")
    print("-" * 20)
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    get_system_info()
