from math import sqrt


n,x=list(map(int,input().split()))
l=list(map(int,input().split()))
opr=list(map(int,input().split()))

def isPrime(n:int):
    if n<=1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

for i in range(n):
    if opr[i]==1:
        if isPrime(l[i])==True:
            if l[i]%2==0:
                print(0,end=" ")
            else:
                print(5,end=" ")
        else:
            print(-1,end=" ")
    else:
        print(0,end=" ")