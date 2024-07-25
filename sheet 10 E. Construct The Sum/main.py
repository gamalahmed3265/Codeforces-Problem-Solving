for _ in range(int(input())):
    n, s = map(int, input().split())
    
    if (n * (n + 1)) // 2 < s:
        print(-1)
        continue

    ans = []

    for i in range(n,0,-1):
        if s-i >= 0:
            s -= i
            ans.append(i)

    print(len(ans), *ans)