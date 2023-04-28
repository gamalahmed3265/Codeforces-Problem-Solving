def diagonal_difference(array):

  primary_diagonal = 0
  secondary_diagonal = 0

  for i in range(len(array)):
    primary_diagonal += array[i][i]
    secondary_diagonal += array[i][-i - 1]

  return abs(primary_diagonal - secondary_diagonal)


def main():
  n = int(input())
  array = []
  for _ in range(n):
    array.append(list(map(int, input().split())))

  print(diagonal_difference(array))


if __name__ == "__main__":
  main()