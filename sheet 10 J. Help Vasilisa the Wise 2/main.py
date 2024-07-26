r1,r2=list(map(int,input().split()))
c1,c2=list(map(int,input().split()))
d1,d2=list(map(int,input().split()))

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
                    if a+b==r1 and c+d==r2 and a+c==c1 and b+d==c2 and a+d==d1 and b+c==d2:
                        print(a,b,c,d)
                        exit()

print(-1)