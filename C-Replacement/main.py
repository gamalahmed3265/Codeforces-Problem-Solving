n = int(input())
a = list(map(int, input().split()))
 
for i in range(n):
    if a[i] < 0:
        a[i]=2
    elif a[i] > 0:
        a[i]=1
    else:
        a[i]=0
print(*a)