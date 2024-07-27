def find_max_difference(N, A):
    min_indices = [0] * N
    min_indices[0] = 0
    for i in range(1, N):
        if A[i] < A[min_indices[i - 1]]:
            min_indices[i] = i
        else:
            min_indices[i] = min_indices[i - 1]

    max_indices = [0] * N
    max_indices[N - 1] = N - 1
    for i in range(N - 2, -1, -1):
        if A[i] > A[max_indices[i + 1]]:
            max_indices[i] = i
        else:
            max_indices[i] = max_indices[i + 1]

    # Find the maximum j - i for A[i] <= A[j]
    max_diff = 0
    i, j = 0, 0
    while i < N and j < N:
        if A[min_indices[i]] <= A[max_indices[j]]:
            max_diff = max(max_diff, max_indices[j] - min_indices[i])
            j += 1
        else:
            i += 1

    return max_diff

# Example usage
N = int(input())
A = list(map(int, input().split()))
print(find_max_difference(N, A))
