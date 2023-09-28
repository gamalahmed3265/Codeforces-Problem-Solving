def find_hello_subsequence(s):
    target = "hello"
    i = 0  
    for char in s: #ahhellllloou
        if char==target[i]:
            i+=1
            if i==len(target):
                return "YES"

    return "NO"

S = input().strip()

result = find_hello_subsequence("ahhellllloou")
print(result)
