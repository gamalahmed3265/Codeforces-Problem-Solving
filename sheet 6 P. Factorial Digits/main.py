import math

def factorial(N:int)->int:
    return math.factorial(N)
def pFactorialDigits(N:int)->int:
    return len(str(factorial(N)))

def main():
    n=int(input())
    print(f"Number of digits of {n}! is {pFactorialDigits(n)}")
    
if __name__ =="__main__":
    main()