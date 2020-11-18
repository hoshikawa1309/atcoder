R, C, K = map(int, input().split())
stage = [[0] * C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    stage[r - 1][c - 1] = v
dp = []
for _ in range(R + 1):
    dp.append([[0] * 4 for _ in range(C + 1)])


for row in range(1, R + 1):
    for column in range(1, C + 1):
        v = stage[row - 1][column - 1]
        for k in range(4):
            if row != 0:
                # 行を移動し、最大保持数をリセット
                # 移動後アイテムを拾う
                dp[row][column][0] = max(dp[row][column][0], dp[row - 1][column][k])
                dp[row][column][1] = max(dp[row][column][1], dp[row - 1][column][k] + v)
            if column != 0:
                # アイテムを拾わない
                dp[row][column][k] = max(dp[row][column][k], dp[row][column - 1][k])
                if k != 0:
                    # アイテムを拾う
                    dp[row][column][k] = max(dp[row][column - 1][k - 1] + v, dp[row][column][k])
ans = 0
for row in range(1, R + 1):
    for column in range(1, C + 1):
        for k in range(4):
            ans = max(ans, dp[row][column][k])
print(ans)
