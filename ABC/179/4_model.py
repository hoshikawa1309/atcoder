N, K = map(int, input().split())
sections = [list(map(int, input().split())) for _ in range(K)]
dp = [0] * N
dp[0] = 1
dpsum = [0] * (N + 1)
dpsum[1] = 1
MOD = 998244353
for i in range(1, N):
    for l, r in sections:
        left = max(0, i - r)
        right = max(0, i - l + 1)
        dp[i] += dpsum[right] - dpsum[left]
    dpsum[i + 1] = (dpsum[i] + dp[i]) % MOD

print(*dp)
print(*dpsum)
print(dp[-1])