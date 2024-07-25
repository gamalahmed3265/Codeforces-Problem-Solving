import math

n=int(input())
a=list(map(int,input().split()))

def prodcts():
    results=0
    for i in range(n):
        results+=math.log10(a[i])
    return results
x=int(math.pow(10,(prodcts()/n)))+1
print(x)
