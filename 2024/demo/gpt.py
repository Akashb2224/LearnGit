def fibonacci(n):
    a, b = 0, 1
    sequence = []
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = 10
print(f"Fibonacci sequence up to {n} terms: {fibonacci(n)}")
