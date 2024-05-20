# Read input
n = int(input().strip())

# Option 1: Keep the number as is
option1 = n

# Option 2: Remove the last digit
option2 = int(str(n)[:-1])

# Option 3: Remove the second to last digit
option3 = int(str(n)[:-2] + str(n)[-1])

# Find the maximum of the three options
max_balance = max(option1, option2, option3)

# Print the result
print(max_balance)
