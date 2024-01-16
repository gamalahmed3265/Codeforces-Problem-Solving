def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))

# Read input value
N = int(input())

# Generate Pascal's Triangle
pascals_triangle = generate_pascals_triangle(N)

# Print the result
print_pascals_triangle(pascals_triangle)
