l=list(map(int,input().split()))

n1=l[0]
n2=l[1]
n3=l[2]
re=l[3]

if ((n1*n2)+n3)==re:
    print("YES")
elif ((n1*n2)-n3)==re:
    print("YES")
elif (n1+(n2*n3))==re:
    print("YES")
elif n1-(n2*n3)==re:
    print("YES")
elif n1+n2-n3==re:
    print("YES")
elif n1-n2+n3==re:
    print("YES")    
else :
    print("NO")