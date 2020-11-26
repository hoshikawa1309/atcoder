N, K = map(int, input().split())
jump = []
MOD = 998244353
for _ in range(K):
    l, r = map(int, input().split())
    jump.append([l, r])
jump.sort()
dp = [0] * N
dp[0] = 1
dp_sum = [0] * (N + 1)
dp_sum[1] = 1
for i in range(1, N):
    for l, r in jump:
        max_val = max(0, i - l + 1)
        min_val = max(0, i - r)
        dp[i] += dp_sum[max_val] - dp_sum[min_val]
    dp[i] %= MOD
    dp_sum[i + 1] = dp[i] + dp_sum[i]
    dp_sum[i + 1] %= MOD
# print(dp)
# print(dp_sum)
print(dp[-1])
