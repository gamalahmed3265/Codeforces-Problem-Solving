al=str(input())

alNum=ord(al.lower())
alNum+=1

if (alNum>=97 and alNum<=122):    
    print(chr(alNum))
else:
    
    print(chr(alNum-26))