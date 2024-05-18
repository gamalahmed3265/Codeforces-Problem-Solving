def find_gift_givers(n, friends):
    gift_givers = [None] * n  # Initialize an empty list to store gift givers

    # Iterate through friends and assign givers
    for i in range(n):
        giver = friends[i]  # Friend who gave a gift to friend i
        print(giver)
        gift_givers[giver - 1] = i + 1  # Assign friend i+1 as the giver (accounting for 0-based indexing)
        print(gift_givers)

    return gift_givers

# Get input
# n = int(input())
# friends = list(map(int, input().split()))
n=4
friends=[2,3,4,1]
# Find gift givers
gift_givers = find_gift_givers(n, friends)

# Print results
print(" ".join(map(str, gift_givers)))
