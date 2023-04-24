
counter=int(input())

for con in range(counter):
	size=int(input())
	arr=list(map(int,input().split()))
	for item in arr:
		print(item,end=" ")
	i=0
	z = 0
	ma=int()
	while True: 
		if z == size - 1:
			break 

		if i == z:
			ma = max(arr[i],arr[i+1])
		else:
			ma = max(ma,arr[i+1])
		
		print(ma,end=" ")
		
		i+=1
		if i == size - 1:
			z+=1
			i=z
	print()
    