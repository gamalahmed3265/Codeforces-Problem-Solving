def longest_uncommon_subsequence_length(a: str, b: str) -> int:
    if a == b:
        return -1
    else:
        return max(len(a), len(b))

# Reading input
a = input().strip()
b = input().strip()

# Getting the result
result = longest_uncommon_subsequence_length(a, b)

# Printing the result
print(result)
