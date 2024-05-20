def min_seconds(n,heights:list):
    # Find the index of the first occurrence of the maximum height
    max_height = max(heights)
    max_index = heights.index(max_height)
    
    # Find the index of the last occurrence of the minimum height
    min_height = min(heights)
    min_index = len(heights) - 1 - heights[::-1].index(min_height)
    
    # If max_index is before min_index, no overlap in swaps
    if max_index > min_index:
        return max_index + (n - 1 - min_index) - 1
    else:
        return max_index + (n - 1 - min_index)

n = int(input())
heights = list(map(int, input().split()))

print(min_seconds(n, heights))