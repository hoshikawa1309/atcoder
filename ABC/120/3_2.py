S = list(input())
now = 0
ans = 0
while now < len(S) - 1:
    if S[now] != S[now + 1]:
        for _ in range(2):
            S.pop(now)
        now = max(0, now - 1)
        ans += 2
    else:
        now += 1
print(ans)