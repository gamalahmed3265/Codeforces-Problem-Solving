import math

n=int(input())
l=list(map(int,input().split()))

def isPrime(k):
    if k<=1:
        return 0
    for i in range(2,int(math.sqrt(k))+1):
        if k%i==0:
            return 0
    return 1
for i in l:
    a=int(math.sqrt(i))
    if a * a==i and isPrime(a):
        print("YES")
    else:
        print("NO")