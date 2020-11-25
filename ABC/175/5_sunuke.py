R, C, K = map(int, input().split())
stage = [[0] * C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    stage[r - 1][c - 1] = v
dp = []
for _ in range(R + 1):
    dp.append([[0] * 4 for _ in range(C + 1)])


for row in range(R):
    for column in range(C):
        v = stage[row][column]
        for k in range(2, -1, -1):
            # 移動後アイテムを拾う
            dp[row][column][k + 1] = max(dp[row][column][k + 1], dp[row][column][k] + v)
        for k in range(4):
            # 移動する
            dp[row + 1][column][0] = max(dp[row][column][k], dp[row + 1][column][0])
            dp[row][column + 1][k] = max(dp[row][column][k], dp[row][column + 1][k])
ans = 0
print(dp)
for k in range(4):
     ans = max(ans, dp[R - 1][C - 1][k])

print(ans)
