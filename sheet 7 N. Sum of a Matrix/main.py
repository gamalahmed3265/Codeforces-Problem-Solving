def nSumofaMatrix(r:int,c:int,a,b)->list:
    return [[a[i][j]+b[i][j] for j in range(c)] for i in range(r)]

r,c=map(int,input().split())

a= [list(map(int,input().split())) for i in range(r)]
b= [list(map(int,input().split())) for i in range(r)]


#nSumofaMatrix(r,c,a,b)
for i in range(r):
    for j in range(c):
        print(nSumofaMatrix(r,c,a,b)[i][j],end=" ")
    print()