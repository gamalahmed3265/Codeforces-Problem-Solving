s = input().strip()

# Initialize variables to keep track of the counts of 'L' and 'R' characters.
count_L = 0
count_R = 0

# Initialize a variable to store the current balanced string.
current_string = ""
result = []

# Iterate through the characters of the input string.
for char in s:
    if char == 'L':
        count_L += 1
    else:
        count_R += 1
    
    current_string += char

    if count_L == count_R:
        result.append(current_string)
        current_string = ""
        count_L = 0
        count_R = 0

print(len(result))
for s in result:
    print(s)
