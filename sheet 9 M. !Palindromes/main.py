def isPalindromes(s:str):
    return s[::]==s[::-1]

def maximalLengthNotPalindrome(s:str):
    n=len(s)
    if len(set(list(s)))==1:
        return 0
    
    if not isPalindromes(s):
        return n
    else: 
        return n-1

print(maximalLengthNotPalindrome(input().strip()))