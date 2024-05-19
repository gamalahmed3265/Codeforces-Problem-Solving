n,x=map(int,input().split())

res=0
for  _ in range(n):
    opt,num=map(str,input().split())
    num=int(num)
    if opt=="+":
        x+=num
    else:
        if num>x:
            res+=1
            continue
        else:
            x-=num
print(x,res)