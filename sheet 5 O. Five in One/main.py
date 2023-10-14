input()
x=[*map(int,input().split())]
d=lambda i:sum(i%j<1 for j in range(1,i))
a=0;b=max(d(i) for i in x)
for i in x:
 if d(i)==b:a=max(i,a)
print(f"The maximum number : {max(x)}\nThe minimum number : {min(x)}\nThe number of prime numbers : {sum(not(any(i%j<1 for j in range(2,i)) or i==1) for i in x)}\nThe number of palindrome numbers : {sum(str(i)==str(i)[::-1] for i in x)}\nThe number that has the maximum number of divisors : {a}")