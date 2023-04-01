l=list(map(int,input().split()))

n1=l[0]
n2=l[1]
n3=l[2]
if n2%n3==0 and n1%n3==0:
    print("Both")
elif n1%n3==0:
    print("Memo")
elif n2%n3==0:
    print("Momo")
else:
    print("No One")