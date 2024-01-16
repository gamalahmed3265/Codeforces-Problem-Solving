def mDivisible(n:int,x:int):
    if n%x==0:
        return True
    else:
        return False

def main():
    n,x=map(int,input().split())
    print("YES" if mDivisible(n,x) else "NO")
    
if __name__ =="__main__":
    main()