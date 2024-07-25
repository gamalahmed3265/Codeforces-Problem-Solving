a=input()
b=input()

def equalStringOneSweap(a,b):
    if(len(a)!=len(b)):
        return False
    if(a==b):
        a=sorted(a)
        for i in range(len(a)-1):
            if(a[i]==a[i+1]):
                return True
        else:
            return False
    else:
        c=0
        for i in range(len(a)):
            if(a[i]!=b[i]):c+=1
        if(c==2 and set(a)==set(b)):
            return True
        else:
            return False

print("YES") if equalStringOneSweap(a,b) else print("NO")