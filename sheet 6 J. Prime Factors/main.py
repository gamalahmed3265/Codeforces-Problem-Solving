N=int(input())

i=2
list_i={}
while N>1:
    if N%i==0:
        N=N//i
        if i in list_i:
            list_i[i]+=1
        else:
            list_i[i]=1
    else:
        i+=1

s=[]
for k,v in list_i.items():
    s.append(f"({k}^{v})")
    
print(*s,sep="*")