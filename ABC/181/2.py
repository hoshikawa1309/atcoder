N = int(input())
ans = 0
dp = [0] * (10 ** 6 + 1)
dp[1] = 1
for i in range(1, len(dp)):
    dp[i] = dp[i - 1] + i
# print(dp[-10:])
for _ in range(N):
    a, b = map(int, input().split())
    ans += dp[b] - dp[a - 1]
print(ans)