n, k = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, n * 2, 2):
    if arr[i] - arr[i - 1] > 1 and arr[i] - arr[i + 1] > 1:
        arr[i] -= 1
        k -= 1
        if k == 0:
            break
print(*arr)
