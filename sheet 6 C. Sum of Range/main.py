n, m = map(int, input().split())
if n > m: n, m = m, n

sumi = m*(m+1)//2 - n*(n-1)//2
if n%2 == 1: n+=1

even_sum = m//2 * (m//2 +1) - n//2 *(n//2 - 1)

print(sumi, even_sum, sumi - even_sum, sep="\n")