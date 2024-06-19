def find_minimum_difference(n, m, pieces):
    pieces.sort()
    min_diff = float('inf')
    
    for i in range(m - n + 1):
        current_diff = pieces[i + n - 1] - pieces[i]
        if current_diff < min_diff:
            min_diff = current_diff
            
    return min_diff

# Read input
n, m = map(int, input().split())
pieces = list(map(int, input().split()))

# Find and print the minimum difference
print(find_minimum_difference(n, m, pieces))
