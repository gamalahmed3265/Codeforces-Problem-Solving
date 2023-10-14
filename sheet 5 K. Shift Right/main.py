def right_shift_array(arr, x):
    n = len(arr)
    x = x % n  # Ensure x is within the range [0, n)

    # Create a new array with the shifted elements
    shifted_array = [0] * n
    for i in range(n):
        shifted_index = (i + x) % n
        shifted_array[shifted_index] = arr[i]

    return shifted_array

# Input
N, X = map(int, input().split())
arr = list(map(int, input().split()))

# Call the function and print the result
result = right_shift_array(arr, X)
print(*result)
