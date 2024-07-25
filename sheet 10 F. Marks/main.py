n,m =list(map(int,input().split()))
l=[]
c=set()
for _ in range(n):
    l.append([ int(x) for x in list(input())])

for i in range(m):
    x=[l[k][i] for k in range(n)]
    search=max(x)
    for w in range(n):
        if x[w]==search:
            c.add(w)
            
print(len(c))