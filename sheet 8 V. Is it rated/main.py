# Reading input
n = int(input())
participants = [tuple(map(int, input().split())) for _ in range(n)]

# Check if the round is rated
rated = False
for a, b in participants:
    if a != b:
        rated = True
        break

if rated:
    print("rated")
else:
    # Check if the ratings are in non-increasing order
    unrated = False
    for i in range(n - 1):
        if participants[i][0] < participants[i + 1][0]:
            unrated = True
            break
    
    if unrated:
        print("unrated")
    else:
        print("maybe")
