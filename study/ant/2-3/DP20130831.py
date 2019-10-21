from pprint import pprint
n = int(input())
point = list(map(int, input().split()))
dp = [[0] * (sum(point) + 1) for i in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    pprint(dp)
    for j in range(sum(point) + 1):
        if j < point[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - point[i - 1]])
pprint(dp)
print(dp[n].count(1))