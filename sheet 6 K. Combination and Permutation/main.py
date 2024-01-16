def factorial(n:int)->int:
    results=1
    for i in range(1,n+1):
        results*=i
    return results

def NCR(n,r)->int:
    return factorial(n)/(factorial(r)*factorial(n-r))
def NPR (n,r)->int:
    return factorial(n)/factorial(n-r)

n,r=map(int,input().split())

print(int(NCR(n,r)),int(NPR(n,r)),sep=" ")