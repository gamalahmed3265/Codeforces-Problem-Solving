def can_form_triangle(n:int, segments:list):
    segments.sort()
    for i in range(n - 2):
        if segments[i] + segments[i + 1] > segments[i + 2]:
            return "YES"
    return "NO"

n = int(input())
segments = list(map(int, input().split()))

result = can_form_triangle(n, segments)
print(result)
