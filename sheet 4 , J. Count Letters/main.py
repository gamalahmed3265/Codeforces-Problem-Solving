def countLetters(a:str)->dict:
    char_count={}
    for cr in a:
        if cr in char_count:
            char_count[cr]+=1
        else:
            char_count[cr]=1
    return char_count

def showData(inpt:dict):
    count_sorted=sorted(inpt.keys())
    
    for cr in count_sorted:
        print(f"{cr} : {inpt[cr]}")
        
count=countLetters(input())
showData(count)

