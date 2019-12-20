S = list(input())
now = S[0]
ans = 0
for i in range(1,len(S)):
    if now != S[i]:
        ans += 1
        now = S[i]
print(ans)