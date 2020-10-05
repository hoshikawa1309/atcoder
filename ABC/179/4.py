N, K = map(int, input().split())
jump = []
for _ in range(K):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        jump.append(i)
jump.sort()
# print(jump)
MOD = 998244353
dp = [0] * N
dp[0] = 1
for i in range(1, N):
    for j in jump:
        if i < j:
            break
        if dp[i - j]:
            dp[i] += dp[i - j]
            dp[i] %= MOD
# print(dp)
print(dp[-1])