def balance_scales(scales, remaining_weights):
    left, right = scales.split('|')
    left_len = len(left)
    right_len = len(right)
    
    diff = abs(left_len - right_len)
    
    if (len(remaining_weights) - diff) % 2 != 0 or len(remaining_weights) < diff:
        return "Impossible"
    
    if left_len < right_len:
        left += remaining_weights[:diff]
    else:
        right += remaining_weights[:diff]
    
    remaining_weights = remaining_weights[diff:]
    half = len(remaining_weights) // 2
    left += remaining_weights[:half]
    right += remaining_weights[half:]
    
    return left + '|' + right

scales = input().strip()
remaining_weights = input().strip()

print(balance_scales(scales, remaining_weights))
