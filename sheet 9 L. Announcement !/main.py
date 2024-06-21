n=int(input())
l=list(map(int, input().strip().split()))
k=set(l)
if len(l)-len(k)==0:
    print(-1)
else:    
    print(len(l)-len(k))