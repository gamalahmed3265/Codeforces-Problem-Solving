# Read input values
n, k = map(int, input().split())
numbers = [input().strip() for _ in range(n)]

# Function to check if a number is k-good
def is_k_good(number, k):
    required_digits = set(str(d) for d in range(k + 1))
    print(required_digits)
    digits_in_number = set(number)
    print(digits_in_number)
    return required_digits.issubset(digits_in_number)

# Count the number of k-good numbers
count_k_good_numbers = sum(is_k_good(number, k) for number in numbers)

# Print the result
print(count_k_good_numbers)
