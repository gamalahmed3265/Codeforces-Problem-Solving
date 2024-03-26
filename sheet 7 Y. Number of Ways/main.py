def count_ways(S, E):
    # Base cases
    if S == E:
        return 1
    if S > E:
        return 0
    
    # Recursive cases: sum of ways for 1 step, 2 steps, and 3 steps
    return count_ways(S + 1, E) + count_ways(S + 2, E) + count_ways(S + 3, E)

S, E = map(int, input().split())

print(count_ways(S, E))
