
from math import sqrt

def isPrime(n:int)->bool:

	if (n <= 1):
		return False

	for i in range(2, int(sqrt(n))+1):
		if (n % i == 0):
			return False

	return True

n=int(input())

if isPrime(n):
	print("YES")
else:
	print("NO")

