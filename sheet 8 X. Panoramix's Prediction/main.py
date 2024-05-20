def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime_after(x):
    num = x + 1
    while True:
        if is_prime(num):
            return num
        num += 1

# Reading input
n, m = map(int, input().strip().split())

# Find the next prime after n
next_prime = next_prime_after(n)

# Compare with m
if next_prime == m:
    print("YES")
else:
    print("NO")
