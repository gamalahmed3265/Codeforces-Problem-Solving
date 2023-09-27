n=int(input())

for i in range(n):
    a=input()
    if len(a)<=10:
        print(a)
    else:
        print(f"{a[0]}{len(a[1:-1])}{a[-1]}")