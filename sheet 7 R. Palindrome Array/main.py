def rPalindromeArray(a:list)->bool:
    return a[::]==a[::-1]

n=int(input())
a=list(map(int,input().split()))

if rPalindromeArray(a)==True:
    print("YES")
else:    
    print("NO")