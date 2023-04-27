
size=int(input())
n=list(map(int,input().split()))
 
assert len(n)==size

def fib(n):
    ans=0
    
    while all(i%2==0 for i in n):
        ans+=1
        n=[i//2 for i in n]
    return ans
print(fib(n))


