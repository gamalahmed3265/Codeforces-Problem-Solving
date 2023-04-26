
size=int(input())
arr=list(map(int,input().split()))


def swap_min_max(arr):
    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))
    arr[min_idx], arr[max_idx] = arr[max_idx], arr[min_idx]
    return arr

for i in swap_min_max(arr):
    print(i,end=" ")
