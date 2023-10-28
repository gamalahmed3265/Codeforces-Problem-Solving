
nums = list(map(int, input().split()))

if nums[-1]%3: print(nums[nums[-1]%3 - 1])
else : print(nums[0] ^ nums[1])