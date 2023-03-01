

wall=int(input("Enter the Wall: "))
numPersone=int(input("Enter the number of friends: "))
reults=0

while numPersone !=0:
    fh=int(input("Enter the hights each one: "))
    if fh>wall:
        reults+=2
    else:
        reults+=1
    numPersone-=1
print(reults)