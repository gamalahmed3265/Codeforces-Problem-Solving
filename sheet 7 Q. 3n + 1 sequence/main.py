def odd(n:int)->int:
    return 3*n+1
def even(n:int)->int:
    return n//2

counter=1
def nSumofaMatrix(n:int)->int:
    global counter
    if n<=1:
        return counter
    else:
        counter+=1
        if n%2!=0:
            return nSumofaMatrix(odd(n))
        else:
            return nSumofaMatrix(even(n))

print(nSumofaMatrix(int(input())))
