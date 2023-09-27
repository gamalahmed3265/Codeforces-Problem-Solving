a=input()
a=a.replace(","," ")

for i in a:
    if i.islower():
        print(i.capitalize(),end="")
    else:
        print(i.lower(),end="")

