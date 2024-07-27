def paint_eggs(n):
    base_pattern = "ROYGBIV"
    additional_pattern = "GBIV"
    
    result = base_pattern
    remaining_length = n - 7
    
    while remaining_length > 0:
        result += additional_pattern[:remaining_length]
        remaining_length -= len(additional_pattern)
    
    return result

# Example usage
n = int(input())
print(paint_eggs(n))
