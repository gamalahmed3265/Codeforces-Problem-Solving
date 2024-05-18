l,b=map(int,input().split())
y=0

while l<= b:
    y+=1    
    l*=3
    b*=2
    
print(y)