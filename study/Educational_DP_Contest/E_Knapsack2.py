N, W = map(int, input().split())
items = []
for _ in range(N):
    items.append(list(map(int, input().split())))
dp = [[float('inf')] * (10 ** 3 + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    weight = items[i - 1][0]
    value = items[i - 1][1]
    for j in range(10 ** 3 + 1):
        if j < value:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - value] + weight)
ans = 0
for i in range(10 ** 3 + 1):
    if dp[-1][i] <= W:
        ans = i
print(*dp, sep='\n')
print(ans)