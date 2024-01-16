
def isValid(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def area(a,b,c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def isTriangle(a,b,c):
    if isValid(a,b,c):
        print("Valid")
        print(area(a,b,c))
    else:
        print("Invalid")
    

def main():
    a,b,c=map(int,input().split())
    
    isTriangle(a,b,c)

if __name__ =="__main__":
    main()