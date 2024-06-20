def calculate_min_max_costs(n, x):
    results = []
    for i in range(n):
        if i==0:
            mini=abs(x[i]-x[i+1])
        elif i==n-1:
            mini=abs(x[i]-x[i-1])
        else:
            mini=min(abs(x[i]-x[i-1]),abs(x[i]-x[i+1]))
        maxi=max(abs(x[i]-x[0]),abs(x[i]-x[-1]))
        results.append((mini,maxi))
    return results

n = int(input())
x = list(map(int, input().split()))

results = calculate_min_max_costs(n, x)
for mini, maxi in results:
    print(mini, maxi)
