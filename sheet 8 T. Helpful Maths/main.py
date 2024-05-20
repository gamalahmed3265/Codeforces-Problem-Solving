text=input().strip()
l=text.split("+")
k=[]
for i in l:
    k.append(int(i))
sortl=sorted(k)

for i in range(len(sortl)):
    if i==len(sortl)-1:
        print(sortl[i],end="")
    else:
        print(sortl[i],end="+")
    
