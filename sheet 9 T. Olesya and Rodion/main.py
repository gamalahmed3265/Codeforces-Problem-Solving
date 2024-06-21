def findNumber(n,t):
    lower=10**(n-1)
    upper=10**n-1
    
    for i in range(lower,upper):
        if i%t==0:
            return i
    return -1

n,t=map(int,input().split())
print(findNumber(n,t))