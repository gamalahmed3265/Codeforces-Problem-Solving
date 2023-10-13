Key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"

Original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def encrypting(s:str):
    for i in s:
        print(Key[Original.index(i)],end="")

def decrypting(s:str):
    for i in s:
        print(Original[Key.index(i)],end="") 

n=int(input())

s=input()
if n==1:
    encrypting(s)
else:
    decrypting(s)