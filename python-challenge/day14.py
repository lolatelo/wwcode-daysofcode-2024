def fibonacci(n):
    """Print the first n numbers of the Fibonacci sequence."""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example usage
fibonacci(10)  # Print the first 10 numbers of the Fibonacci sequence
