s=input()
s=s[s.index("username"):]


for i in s.split("&"):
    print(i.replace("="," : "))