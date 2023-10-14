def printTime(n,ch):
    for i in range(n):
        if i==n:
            print(i,end="")
        else:
            print(ch,end=" ")


size=int(input())

for i in range(size):
    l=list(map(str,input().split()))
    
    printTime(int(l[0]),l[1])
    print()


