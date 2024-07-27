for _ in range(int(input())):
    s=list(input())
    t=list(input())
    p=list(input())
    ok=True
    for i in range(len(t)):
        if len(s)>0 and t[i]==s[0]:
            del s[0]
        elif t[i] not in p:
            ok=False
            break
        else:
            del p[p.index(t[i])]
    print("YES"if ok and len(s)==0 else"NO")