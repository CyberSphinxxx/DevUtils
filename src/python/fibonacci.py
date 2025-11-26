import sys

def fibonacci(n):
    """Generates the first n Fibonacci numbers."""
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fibonacci.py <count>")
    else:
        try:
            count = int(sys.argv[1])
            print(f"First {count} Fibonacci numbers: {fibonacci(count)}")
        except ValueError:
            print("Please provide a valid integer.")
