def max_path_sum(matrix, i, j):
    # Base cases
    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        return matrix[i][j]
    
    # Recursive cases
    if j < len(matrix[0]) - 1 and i < len(matrix) - 1:
        right = max_path_sum(matrix, i, j + 1)
        down = max_path_sum(matrix, i + 1, j)
        return matrix[i][j] + max(right, down)
    elif j < len(matrix[0]) - 1:
        return matrix[i][j] + max_path_sum(matrix, i, j + 1)
    elif i < len(matrix) - 1:
        return matrix[i][j] + max_path_sum(matrix, i + 1, j)
        
        
# Read input
N, M = map(int, input().split())

matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

result = max_path_sum(matrix,0,0)

print(result)

