def count_magnet_groups(n, magnets):
    group_count = 1  # At least one group since there's at least one magnet

    for i in range(1, n):
        if magnets[i] != magnets[i - 1]:
            group_count += 1

    return group_count

n = int(input())
magnets = [input().strip() for _ in range(n)]

print(count_magnet_groups(n, magnets))
