import math

def determine_shape(R, S):
    diagonal_of_square = S * math.sqrt(2)
    diameter_of_circle = 2 * R

    if diagonal_of_square <= diameter_of_circle:
        return "Circle"
    elif diameter_of_circle <= S:
        return "Square"
    else:
        return "Complex"

R, S = map(int, input().split())
result = determine_shape(R, S)
print(result)
