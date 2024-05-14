s = list(input())
for i in range(len(s)):
	if s[i] == '?':
		s[i] = s[-i-1] if s[-i-1] != '?' else 'a'
print("".join(s)) if s == s[::-1] else print(-1)