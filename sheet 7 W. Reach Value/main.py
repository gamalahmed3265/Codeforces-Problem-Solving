def multiply10(n:int)->int:
    return n*10
def multiply20(n:int)->int:
    return n*20

def can_reach_value(current_value, target):
    if current_value == target:
        return True
    if current_value > target:
        return False
    return can_reach_value(multiply10(current_value), target) or can_reach_value(multiply20(current_value), target)

T = int(input())
for _ in range(T):
    N = int(input())
    if can_reach_value(1, N):
        print("YES")
    else:
        print("NO")
