t, cnt = int(input()), 0
for i in range(t):
    n = int(input())
    if n%2==0:
        print(n//2)
    else:
        if cnt%2==0:
            print(n//2+1)
        else:
            print(n//2)
        cnt+=1

