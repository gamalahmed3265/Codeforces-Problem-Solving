t=str(input())

def isILuckyNumbers(nums):
    n1=int(nums[0])
    n2=int(nums[1])
    if n2==0:
        return "YES"
    if n1%n2 ==0 or n2% n1==0  :
        return "YES"
    else :
        return "NO"
        
print(isILuckyNumbers(t))