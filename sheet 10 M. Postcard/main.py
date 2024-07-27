s=list(input())
FinalLen=int(input())
snow,candy=[],[]
for i in range(len(s)):
    if s[i]=='*':
        snow.append(i)
    elif s[i]=='?':
        candy.append(i)

ActLen=len(s)-len(candy)-len(snow)
if ActLen >=FinalLen:
    while ActLen >FinalLen and len(candy):
        index=candy.pop()
        s[index-1]='?'
        ActLen-=1
    
    while ActLen >FinalLen and len(snow):
        index=snow.pop()
        s[index-1]='?'
        ActLen-=1

else:
    NeededLen=FinalLen-ActLen+1
    if snow!=[]:
        index=snow[0]
        s[index-1]=s[index-1]*NeededLen
        ActLen=FinalLen

if ActLen ==FinalLen:
        for i in s:
            if i not in ['?','*']:
                print(i,end='')
else:
    print('Impossible')

