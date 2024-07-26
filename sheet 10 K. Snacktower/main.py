size =int(input())
arr=[0]*(size+1)

curr=size
nums=list(map(int,input().split()))
for i in range(size):
    arr[nums[i]]=1
    while arr[curr]:
        print(curr,end=" ")
        curr-=1
    print()
