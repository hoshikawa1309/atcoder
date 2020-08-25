def gcd(a, b, c):
    if b == 0:
        return c
    return gcd(b, a % b, c + 1)


K = int(input())
dp = [0] * (K + 2)
dp[0], dp[1] = 1, 1
for i in range(K):
    dp[i + 2] = dp[i + 1] + dp[i]
print(dp[-1], dp[-2])
# print(gcd(dp[-1], dp[-2], 0))
