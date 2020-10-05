s = int(input())
dp = [0] * (s + 1)
dp[0] = 1
MOD = 10 ** 9 + 7
for i in range(s + 1):
    for j in range(i - 3 + 1):
        dp[i] += dp[j]
        dp[i] %= MOD
print(*dp)
print(dp[s])