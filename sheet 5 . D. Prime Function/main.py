
from math import sqrt

def isPrime(n:int)->bool:

	if (n <= 1):
		return False

	for i in range(2, int(sqrt(n))+1):
		if (n % i == 0):
			return False

	return True

t=int(input())
for i in range(t):
    num=int(input())
    if isPrime(num):
        print("YES")
    else:
        print("NO")