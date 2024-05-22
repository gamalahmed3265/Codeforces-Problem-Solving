(r,c,t)=[int(x) for x in input().split()]
l=[]
for i in range(r):
    l.append(list('.'*c))
for i in range(t):
    (r1,c1,r2,c2,a)=[x for x in input().split()]
    for x in range(min(int(r1),int(r2))-1,max(int(r1),int(r2))):
        for z in range(min(int(c1),int(c2))-1,max(int(c1),int(c2))):
            l[x][z]=a
for i in l:
    print(*i,sep='')