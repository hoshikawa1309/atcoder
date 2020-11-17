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
        for k in range(1, 4):
            # 同じ行でアイテムを拾うことと一つ前の行で拾わないパターンのマックス
            dp[row][column][k] = max(dp[row][column - 1][k - 1] + v, dp[row - 1][column][k])
print(dp)
print(dp[-1][-1][-1])



