import math

def lcm(a,b):return (a*b)//math.gcd(a,b)
a,b,c,d=map(int,input().replace(" ","/").split("/"))

print(str(lcm(a,c))+"/"+str(math.gcd(b,d)))