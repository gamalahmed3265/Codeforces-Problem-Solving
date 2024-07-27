n,m,k=list(map(int,input().split()))
c = 0
mi = min((n, m, k))
c += mi
n-=mi;m-=mi;k-=mi
c += min(n//2, k)
print(c)