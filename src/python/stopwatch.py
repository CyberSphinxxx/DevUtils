import time
import sys

def stopwatch():
    """Simple CLI stopwatch."""
    print("Press ENTER to start. Press CTRL+C to stop.")
    input()
    start_time = time.time()
    print("Started...")
    try:
        while True:
            time.sleep(0.1)
            elapsed = time.time() - start_time
            sys.stdout.write(f"\rElapsed: {elapsed:.2f}s")
            sys.stdout.flush()
    except KeyboardInterrupt:
        print(f"\nStopped. Total time: {elapsed:.2f}s")

if __name__ == "__main__":
    stopwatch()
