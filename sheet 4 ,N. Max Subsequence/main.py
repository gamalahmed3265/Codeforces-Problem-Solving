n=int(input())
s=input().strip()

k=0

for char in s:
    if char!=char_index:
        k+=1
        char_index=char

print(k)