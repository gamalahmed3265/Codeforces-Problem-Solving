n = int(input())
a = list(map(int, input().split()))

max_f = 0
for x in a:
    f = 0
    while x % 2 == 0:
        f += 1
        x //= 2
    max_f = max(max_f, f)

print(max_f)