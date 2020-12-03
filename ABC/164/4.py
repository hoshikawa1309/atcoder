s = list(input())
s = s[::-1]
n = len(s)
x = 1
tot = 0
ans = 0
mod = 2019
cnt = [0] * (mod + 1)

for i in range(n):
    cnt[tot] += 1
    tot += int(s[i]) * x
    tot %= mod
    ans += cnt[tot]
    x = x * 10 % mod
print(cnt)
print(ans)