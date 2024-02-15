N=int(input())


def printRecursion(n:int):
    if n==0:
        return
    else:
        print("I love Recursion")
        printRecursion(n-1)
    
    
printRecursion(N)