r ,c = list(map(int, input().split()))
arr_row = [0]*r
arr_col = [0]*c
res = 0
for i in range(r):
    cake = input()
    for j in range(c):
        if cake[j] == 'S':
            arr_row[i] = 1
            arr_col[j] = 1

for k in range(r):
    for y in range(c):
        if arr_row[k] == 0 or arr_col[y] == 0:
            res += 1

print(res)