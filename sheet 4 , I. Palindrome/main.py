def isPalindrome(a:str)->str:
    reverse=a[::-1]
    
    if a==reverse:
        return "YES"
    else:
        return "NO"

a=input()
results=isPalindrome(a)
print(results)