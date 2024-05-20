def untreated_crimes(events):
    available_officers = 0
    untreated_crimes = 0
    
    for event in events:
        if event == -1:
            if available_officers > 0:
                available_officers -= 1
            else:
                untreated_crimes += 1
        else:
            available_officers += event
    
    return untreated_crimes

n=int(input())
nums=list(map(int,input().split()))

print(untreated_crimes(nums))