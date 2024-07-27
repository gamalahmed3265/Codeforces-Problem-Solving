def check(v, newnum):
    add = True
    newnum = newnum[::-1]
    for i in range(len(v)):

        s1 = v[i][::-1]
        for j in range(3):
            if s1[j] != '0' and newnum[j] != '0':
                add = False
                break
            
        if not add:
            break

    return add



k = int(input())
nums = input().split()
for i in range(k):
    if len(nums[i]) == 2:
        nums[i] = '0' + nums[i]
    elif len(nums[i]) == 1:
        nums[i] = '00' + nums[i]

nums = sorted(nums, key=lambda n: (str(int(n)).count('0')), reverse=True)


v = []

for i in range(k):
    if check(v, nums[i]):
        v.append(nums[i])


print(len(v))
for n in v:
    print(int(n), end=" ")
print()