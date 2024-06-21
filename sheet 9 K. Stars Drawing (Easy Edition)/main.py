def find_stars(grid, n, m):
    potential_centers = []

    # Check each cell to see if it can be the center of a star
    for i in range(1, n-1):
        for j in range(1, m-1):
            if grid[i][j] == '*' and grid[i-1][j] == '*' and grid[i+1][j] == '*' and grid[i][j-1] == '*' and grid[i][j+1] == '*':
                potential_centers.append((i, j))

    stars = []
    mark_grid = [['.' for _ in range(m)] for _ in range(n)]

    # Determine the size of each potential center and mark the stars
    for i, j in potential_centers:
        size = 1
        while (i - size >= 0 and i + size < n and j - size >= 0 and j + size < m and
               grid[i-size][j] == '*' and grid[i+size][j] == '*' and
               grid[i][j-size] == '*' and grid[i][j+size] == '*'):
            size += 1
        size -= 1

        if size > 0:
            stars.append((i + 1, j + 1, size))  # Convert to 1-based indexing
            mark_grid[i][j] = '*'
            for k in range(1, size + 1):
                mark_grid[i-k][j] = '*'
                mark_grid[i+k][j] = '*'
                mark_grid[i][j-k] = '*'
                mark_grid[i][j+k] = '*'

    # Check if the marked grid matches the original grid
    for i in range(n):
        for j in range(m):
            if grid[i][j] != mark_grid[i][j]:
                return -1, []

    return len(stars), stars

# Read input
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# Find stars and output the result
num_stars, stars = find_stars(grid, n, m)
if num_stars == -1:
    print(-1)
else:
    print(num_stars)
    for star in stars:
        print(star[0], star[1], star[2])
