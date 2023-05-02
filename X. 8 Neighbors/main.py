def isAllX(A, X, Y):
  """
  Determines whether all neighbors of the given cell are 'x' or not.

  Args:
    A: A 2D array of size N * M which contains 'x' or '.' only.
    X: The row number of the given cell.
    Y: The column number of the given cell.

  Returns:
    A boolean value indicating whether all neighbors of the given cell are 'x' or not.
  """

  isAllX = True
  for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
      if dx != 0 or dy != 0:
        if A[X + dx][Y + dy] != 'x':
          isAllX = False
          break

  return isAllX


def main():
  """
  The main function.
  """

  N, M = map(int, input().split())
  A = [input() for _ in range(N)]

  X, Y = map(int, input().split())

  print("yes" if isAllX(A, X - 1, Y - 1) else "no")


if __name__ == "__main__":
  main()