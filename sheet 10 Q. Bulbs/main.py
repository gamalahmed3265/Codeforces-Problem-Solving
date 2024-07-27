n=int(input())
l=list(map(int, input().split()))

turnOn=0
moments=0
for i in range(n):
    turnOn=max(turnOn,l[i])
    if turnOn==i+1:
        moments+=1
    
print(moments)