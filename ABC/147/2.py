s = list(input())
s_len = len(s)
s_rev = s[::-1]
ans = 0
for i in range(s_len // 2):
    if s[i] != s_rev[i]:
        ans += 1
print(ans)