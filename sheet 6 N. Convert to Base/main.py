def convert_to_decimal(N, X):
  """Converts a number N from base X to decimal."""
  decimal = 0
  power = 0
  for digit in reversed(N):
    value = int(digit, 36) if digit.isalpha() else int(digit)  # Handle digits A-Z
    decimal += value * X**power
    power += 1
  return decimal

def convert_from_decimal(N, X):
  """Converts a decimal number N to base X."""
  result = []
  while N > 0:
    remainder = N % X
    N //= X
    if remainder >= 10:
      result.append(chr(remainder - 10 + ord('A')))  # Use letters for digits 10-35
    else:
      result.append(str(remainder))
  return ''.join(reversed(result))

T = int(input())
N, X = input().split()
X = int(X)

if T == 1:
  print(convert_to_decimal(N, X))
elif T == 2:
  print(convert_from_decimal(int(N), X))
