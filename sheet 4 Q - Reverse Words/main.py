s=input().strip()

def reverse(l:list):
    return l[::-1]


print(" ".join([reverse(i) for i in s.split()]))

