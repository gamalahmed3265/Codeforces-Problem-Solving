def form_teams(n, t):
    programmers = []
    mathematicians = []
    sportsmen = []
    
    # Categorize the children based on their skills
    for i in range(n):
        if t[i] == 1:
            programmers.append(i + 1)  # Store index + 1 because indices are 1-based
        elif t[i] == 2:
            mathematicians.append(i + 1)
        elif t[i] == 3:
            sportsmen.append(i + 1)
    
    # Determine the maximum number of teams
    num_teams = min(len(programmers), len(mathematicians), len(sportsmen))
    
    # Output the number of teams
    print(num_teams)
    
    # Output the teams
    for i in range(num_teams):
        print(programmers[i], mathematicians[i], sportsmen[i])

# Read input
n = int(input())
t = list(map(int, input().split()))

# Form and print teams
form_teams(n, t)
