N, K = map(int, input().split())
jump = []
for _ in range(K):
    l, r = map(int, input().split())
    jump.append([l, r])
jump.sort()
# print(jump)
MOD = 998244353
dp = [0] * (N + 1)
dp[1] = 1
dp_sum = [0] * (N + 1)
dp_sum[1] = 1
for i in range(2, N + 1):
    for l, r in jump:
        min_section = max(0, i - r - 1)
        max_section = max(0, i - l)
        dp[i] += (dp_sum[max_section] - dp_sum[min_section]) % MOD
    dp[i] %= MOD
    dp_sum[i] = (dp[i] + dp_sum[i - 1]) % MOD
print(dp)
print(dp_sum)
print(dp[-1])