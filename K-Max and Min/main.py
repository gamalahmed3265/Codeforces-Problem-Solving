a, b, c = map(int, input().split())

min_num = max_num = a

if b < min_num:
    min_num = b
elif b > max_num:
    max_num = b

if c < min_num:
    min_num = c
elif c > max_num:
    max_num = c

print(min_num, max_num)