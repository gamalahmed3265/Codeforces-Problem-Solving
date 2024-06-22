n,k=map(int,input().split())

count=0

for i in range(n):
    l,r=map(int,input().split())

    count+=(r-l+1)
count%=k
if count==0:
    print(count)
else:
    print(k-count)