def generate_password(n, k):
    letters = [chr(i) for i in range(ord('a'), ord('a') + k)]
    
    password = ''.join(letters * ((n // k) + 1))[:n]
    
    return password

n, k = map(int, input().split())
print(generate_password(n, k))
