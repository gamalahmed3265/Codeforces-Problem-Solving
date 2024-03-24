def can_make_expression(arr, target, current_sum, index, n):
    # Base case: If we have processed all numbers, check if the current sum equals the target
    if index == n:
        return current_sum == target

    # Recursively try adding and subtracting the current number from the current sum
    return (can_make_expression(arr, target, current_sum + arr[index], index + 1, n) or
            can_make_expression(arr, target, current_sum - arr[index], index + 1, n))

# Read input
N, X = map(int, input().split())
A = list(map(int, input().split()))

# Check if it's possible to create an expression that equals X
if can_make_expression(A, X, A[0], 1, N):
    print("YES")
else:
    print("NO")
