nums=list(input())

if 9-int(nums[0])==0:
    print(9,end="")
    del nums[0]
for i in range(len(nums)):
    elem=int(nums[i])
    if (9-elem)<elem:
        print(9-elem,end='')
    else:
        print(elem,end="")
