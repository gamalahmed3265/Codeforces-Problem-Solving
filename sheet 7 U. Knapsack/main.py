def knapsack_recursive(weights, values, W, n):
    if n == 0 or W == 0:
        return 0
    if weights[n-1] > W:
        return knapsack_recursive(weights, values, W, n-1)
    else:
        return max(
            values[n-1] + knapsack_recursive(weights, values, W - weights[n-1], n-1),
            knapsack_recursive(weights, values, W, n-1)
        )
N, W = map(int, input().split())

weights = []
values = []

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
print(knapsack_recursive(weights, values, W, N))