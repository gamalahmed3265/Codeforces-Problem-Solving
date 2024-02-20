n=int(input())

results=1
def factorial(n:int,i:int):
    if i>=n:
        return
    global results
    results*=i
    i+=1
    factorial(n,i)
        
factorial(n+1,1)

print(results)