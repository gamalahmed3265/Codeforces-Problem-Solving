size=int(input())
nums= list(map(int,input().split()))

minEl = nums[0]
counter = 0

for i in range(size):
	if(minEl == nums[i]):
		counter+=1
	if minEl > nums[i]:
		minEl = nums[i]
		counter = 1;

if counter % 2 == 0:
	print("Unlucky")
else: 
    print("Lucky")