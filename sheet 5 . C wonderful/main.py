def isOdd(n:int)->bool:
    return n%2==1

def isPalindrome(n:int)->bool:
        return bin(n)[2:]==bin(n)[2:][::-1]

n=int(input())
if isOdd(n) and isPalindrome(n):
    print("YES")
else:
    print("NO")