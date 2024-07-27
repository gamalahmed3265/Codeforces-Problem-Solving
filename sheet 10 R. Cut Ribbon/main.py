a,b,c,d = map(int,input().split())
l = [0] * (a + 1)
for i in range(1, a + 1):
    l[i] = -1
    for j in [b,c,d]:
        if i - j >= 0 and l[i - j] != -1:
            l[i] = max(l[i], l[i- j] + 1)
print(l[a])