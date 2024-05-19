_ = input()
nums = [int(i) for i in input().split()]
sereja, dima = 0, 0
turn = True

while nums:
    num = max(nums[0], nums[-1])
    nums.remove(num)
    
    if turn:
        sereja += num
    else:
        dima += num
        
    turn = not turn
    
print(sereja, dima)