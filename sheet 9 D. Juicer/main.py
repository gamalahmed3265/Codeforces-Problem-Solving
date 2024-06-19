
nOrg,bMaOragJu,dWastSection=list(map(int,input().split()))
oranges=list(map(int,input().split()))

def juicer():
    sumWastOrange=0
    results=0
    for org in oranges:
        if org<=bMaOragJu:
            sumWastOrange+=org
            if sumWastOrange>dWastSection:
                results+=1
                sumWastOrange=0
    
    return results

print(juicer())