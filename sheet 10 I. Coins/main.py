a="A"
b="B"
c="C"

for i in range(3):
    stmt=input()
    if "A>" in stmt or "<A" in stmt:
        a+="1"
    if "B>" in stmt or "<B" in stmt:
        b+="1"
    if "C>" in stmt or "<C" in stmt:
        c+="1"
l=[a,b,c]
l.sort(key=len)
out="".join(l)
if len(a)==len(b)==len(c):
    print("Impossible")
else:
    print(out.replace("1",""))