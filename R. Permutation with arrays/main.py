def sortArr(arr):
	n=len(arr)
	for i in range(n-1):
		for j in range(n-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
	return arr

def rPermutationWithArrays(arr1:list,arr2:list):
	if len(arr2)!=len(arr2):
		return False
	arr1=sortArr(arr1)
	arr2=sortArr(arr2)
	
	for i in range(len(arr1)):
		if arr1[i]!=arr2[i]:
			return False

	return True

def main():
	n=int(input())
	A=list(map(int,input().split()))
	B=list(map(int,input().split()))
	assert n==len(A)==len(B)
	if rPermutationWithArrays(A,B):
		print("yes")
	else:
		print("no")
if __name__ =="__main__":
    main()