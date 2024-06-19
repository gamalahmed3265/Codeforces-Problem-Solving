def dragons(s:int,listofDragons:list):
    listofDragons.sort(key=lambda x:x[0])
    for x,y in listofDragons:
        if s>x:
            s+=y
        else:
            return "NO"
        
    return "YES"

s,n=map(int,input().split())

listofDragons= [ tuple(map(int,input().split())) for _ in range(n)]
print(dragons(s,listofDragons))    