N=int(input())
A=list(map(int,input().split()))

maxValue=A[0]

for i in range(N):
    if A[i]> maxValue:
        maxValue=A[i]
    print(maxValue,end=" ")