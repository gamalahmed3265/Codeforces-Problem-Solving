def is_palindrome(n):
    return str(n) == str(n)[::-1]

n = int(input())
print(str(n)[::-1].lstrip('0'))
print("YES" if is_palindrome(n) else "NO")