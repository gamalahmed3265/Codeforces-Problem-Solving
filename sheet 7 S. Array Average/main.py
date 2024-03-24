import math

results=0
def sArrayAverage(n:int,a:list)->int:
    global results
    if n<=0:
        return results
    else:
        results+=a[n-1]
        n-=1
        return sArrayAverage(n,a)
n=int(input())
a=list(map(int,input().split()))

print(sArrayAverage(n,a)/n)

###### or 

n,arr = int(input()),list(map(int,input().split()));print(f"{((sum(arr) / n)):.6f}")
