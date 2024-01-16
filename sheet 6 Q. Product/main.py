import math
def factor(l,r):
  if l>r:
    return 1
  return math.factorial(r)//math.factorial(l-1)

def oBigAddMultiply(l,r,m):
  return factor(l,r)%m

def main():
  l,r,m=map(int,input().split())
  print(oBigAddMultiply(l,r,m))
  
if __name__ =="__main__":
  main()