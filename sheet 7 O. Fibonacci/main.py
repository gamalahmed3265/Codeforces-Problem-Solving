def fibonacci(n:int):
    # Base cases
    if n == 1:
        return 0
    elif n == 2:
        return 1
    # Recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example input
N = int(input())

# Calculate the Nth Fibonacci number
fib_number = fibonacci(N)

# Print the result
print(fib_number)
