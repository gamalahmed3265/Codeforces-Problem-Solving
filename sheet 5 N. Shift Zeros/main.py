def shiftToRight(l:list):
    j=0
    for i in range(len(l)):
        if l[i]!=0:
            print(l[i],end=" ")
        else:
            j+=1
    for i in range(j):
        print(0,end=" ")


size=int(input())

l=list(map(int,input().split()))


shiftToRight(l)
