def printNum(n:int)->int:
    for i in range(1,n+1):
        if i!=n:
            print(i,end=" ")
        else:
            print(i,end="")
n=int(input())

printNum(n)