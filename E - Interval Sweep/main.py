l=list(map(int,input().split()))

n1=l[0]
n2=l[1]

if( n1==0 and n2==0 )or abs( n1-n2)>=2:
    print("NO")
else :
    print("YES")