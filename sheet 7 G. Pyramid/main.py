def print_triangle(height):
    for i in range(1, height + 1):
        print(i)
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# Set the height of the triangle
triangle_height = int(input())

# Call the function to print the triangle
print_triangle(triangle_height)
