from collections import Counter

def can_rearrange(n, array):
    freq = Counter(array)
    max_count = max(freq.values())
    if max_count > (n + 1) // 2:
        return "NO"
    else:
        return "YES"

# Read input
n = int(input().strip())
array = list(map(int, input().strip().split()))

# Output the result
print(can_rearrange(n, array))
