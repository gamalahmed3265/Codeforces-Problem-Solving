def determine_winner(n, goals):
    goal_counts = {}
    
    for goal in goals:
        if goal in goal_counts:
            goal_counts[goal] += 1
        else:
            goal_counts[goal] = 1
    winner = max(goal_counts, key=goal_counts.get)
    return winner

n = int(input())
goals = [input().strip() for _ in range(n)]

winner = determine_winner(n, goals)
print(winner)
