vowelWord=['a', 'e', 'i', 'o', 'u']

text=input()

results=0
l=list(text)
def countVowels(l:list,i:int):
    if i>=len(l):
        return    
    if l[i].lower() in vowelWord:
        global results
        results+=1
    i+=1
    countVowels(l,i)


countVowels(l,0)
print(results)


######################## 2

vowelWord=['a', 'e', 'i', 'o', 'u']

text=input()

results=0
for i in list(text):
    if i.lower() in vowelWord:
        results+=1

print(results)