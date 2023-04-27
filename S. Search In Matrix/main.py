def find_number(array, number):
      """
  Determines if number exists in the 2D array array.

  Args:
    array: The 2D array.
    number: The number to search for.

  Returns:
    True if number exists in the array, False otherwise.
  """

  for row in array:
    for element in row:
      if element == number:
        return True

  return False


def main():
  """
  The main function.
  """

  n, m = map(int, input().split())
  array = []
  for _ in range(n):
    array.append(list(map(int, input().split())))

  number = int(input())

  if find_number(array, number):
    print("will not take number")
  else:
    print("will take number")


if __name__ == "__main__":
  main()