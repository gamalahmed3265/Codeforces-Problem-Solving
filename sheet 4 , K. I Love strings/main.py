################## method 1

def concatString(s,t):
    if(len(s)<=len(t)):
        for i in range(len(s)):
            print(f"{s[i]}{t[i]}",end="")
        print(t[i+1:])
    else:
        for i in range(len(t)):
            print(f"{s[i]}{t[i]}",end="")
        print(s[i+1:])
        
size=int(input())
for k in range(size):
    s,t= list(map(str,input().split()))
    concatString(s,t)


################## method 2

def concatenate_strings(s, t):
    result = []
    i, j = 0, 0

    while i < len(s) or j < len(t):
        if i < len(s):
            result.append(s[i])
            i += 1
        if j < len(t):
            result.append(t[j])
            j += 1

    return ''.join(result)

n = int(input())

for _ in range(n):
    s, t = input().split()
    concatenated_string = concatenate_strings(s, t)
    print(concatenated_string)

