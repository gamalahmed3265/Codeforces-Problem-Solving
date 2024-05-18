n=int(input())


def bWatermelon():
    if n<=2:
        print("NO")
        return
    print("YES") if n%2==0  else print("NO")
    
bWatermelon()