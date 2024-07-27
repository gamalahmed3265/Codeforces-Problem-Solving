row,col=list(map(int, input().split()))
matrix=[input() for _ in range(row)]
res=[]
for i in range(row):
    a=[]
    for j in range(col):
        if matrix[i][j]==".":
            if (i+j)%2==0:
                a.append("B")
            else:   
                a.append("W")
        else:
            a.append("-")
    res.append(a)

for _ in range(row):
    print(*res[_],sep="")