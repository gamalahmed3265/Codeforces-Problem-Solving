
size=int(input())
l=list(map(int,input().split()))

def minNums(l:list)->int:
    min_num=l[0]
    for i in range(len(l)):
        if l[i]<min_num:
            min_num=l[i]

    return min_num

def maxNums(l:list)->int:
    man_num=l[0]
    for i in range(len(l)):
        if l[i]>man_num:
            man_num=l[i]

    return man_num
print(minNums(l),maxNums(l))

# or other way
# print(min(l),max(l))