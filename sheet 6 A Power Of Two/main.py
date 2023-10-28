N = int(input())

# Check if N is a power of 2
if N > 0 and (N & (N - 1)) == 0:
    print("YES")
else:
    print("NO")