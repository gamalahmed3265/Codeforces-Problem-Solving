def last_digit_of_1378_power_n(n):
    if n == 0:
        return 1  # Special case for 0 as any number to the power 0 is 1.
    last_digits = [8, 4, 2, 6]
    return last_digits[(n - 1) % 4]

n = int(input().strip())

# Printing the result
print(last_digit_of_1378_power_n(n))

