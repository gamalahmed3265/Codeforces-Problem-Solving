resultsPermutations =1
def permutation(n:int)->int:
    global resultsPermutations
    if n<=1:
        return resultsPermutations
    else:
        return permutation(n-1)*n
    
    
def tCombination(n:int,r:int)->int:
    return permutation(n)//permutation(n-r)//permutation(r)

n,r=list(map(int,input().split()))
print(tCombination(n,r))
