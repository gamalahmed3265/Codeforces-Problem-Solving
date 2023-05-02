def isAllX(A, X, Y):
 
  for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
      if dx != 0 or dy != 0:
        if A[X + dx][Y + dy] != 'x':
          return  False

  return True



N, M = map(int, input().split())
A = [input() for _ in range(N)]

X, Y = map(int, input().split())

print("yes" if isAllX(A, X - 1, Y - 1) else "no")

