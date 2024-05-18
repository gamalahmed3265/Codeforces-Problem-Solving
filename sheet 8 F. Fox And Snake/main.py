def draw_snake(n, m):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print('#' * m)
        elif i % 4 == 0:
            print('#' + '.' * (m - 1))
        else:
            print('.' * (m - 1) + '#')

# Example usage
n, m = map(int,input().split())
draw_snake(n, m)


# ---------------------------------------------------------
# other way

n, m = map(int, input().split())
oddRow = "#" * m
evenRow = "#"+"."*(m-1)
 
for i in range(1,n+1):
    if i % 2 != 0:
        print(oddRow)
    else:
        evenRow = evenRow[len(evenRow)::-1]
        print(evenRow)