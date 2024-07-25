s=input()
t=input()

def deleteFromLeft():
    s_len=len(s)
    t_len=len(t)

    i=0
    
    while i<s_len and i <t_len and s[s_len-1-i]==t[t_len-1-i]:
        i+=1
    
    return (s_len-i)+(t_len-i)

print(deleteFromLeft())