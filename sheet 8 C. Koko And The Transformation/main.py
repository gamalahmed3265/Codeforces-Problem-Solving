n,m=list(map(int,input().split()))

a=list(map(int,input().split()))
b=list(map(int,input().split()))

print("Yes") if sum(a)==sum(b) else print("No")