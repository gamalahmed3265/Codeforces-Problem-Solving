def calculate():
    if n%2==0:
        return n//2
    else:
        return -n//2

n=int(input())
print(calculate())