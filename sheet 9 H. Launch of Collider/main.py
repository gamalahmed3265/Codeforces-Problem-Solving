def first_collision_time(n, directions, positions):
    min_time = float('inf')
    found_collision = False
    
    for i in range(n - 1):
        if directions[i] == 'R' and directions[i + 1] == 'L':
            collision_time = (positions[i + 1] - positions[i]) // 2
            if collision_time < min_time:
                min_time = collision_time
            found_collision = True
    
    if found_collision:
        return min_time
    else:
        return -1

n = int(input())
directions = input().strip()
positions = list(map(int, input().split()))

print(first_collision_time(n, directions, positions))
