from math import pow
def equation(a,b):
    sumEquation=pow(a,0)-1
    powEquation=0
    for i in range(2,b+1,2):
        powEquation+=pow(a,i)
        
    return sumEquation+powEquation

l=list(map(int,input().split()))
[a,b]=l
print(int(equation(a,b)))