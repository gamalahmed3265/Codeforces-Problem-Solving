from math import ceil
def calculate():
    if m>n:
        return -1
    return m*ceil((n-(n//2))/m)
        
n,m=list(map(int,input().split()))
print(calculate())