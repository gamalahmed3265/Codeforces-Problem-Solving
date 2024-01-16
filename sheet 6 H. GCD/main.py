import math

def find_gcd(a:int, b:int)->int:
    """greatest common divisor of A and B.

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    while b:
        a, b = b, a % b
    return a

def find_lcm(a:int, b:int)->int:
    """ the least common multiple of A and B.

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    return abs(a * b) // math.gcd(a, b)

# Read input values
A, B = map(int, input().split())

# Calculate GCD and LCM
gcd_result = find_gcd(A, B)
lcm_result = find_lcm(A, B)

# Print the results
print(gcd_result, lcm_result)
