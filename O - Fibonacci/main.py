
n=int(input())
 
def fib(n):
    start = 0
    sec = 1
    if n==1:
        return start
    elif n==2:
        return sec
    else:
        for i in range(3,n+1):
            res = start + sec
            start = sec
            sec = res
        return sec
    
        
print(fib(n))