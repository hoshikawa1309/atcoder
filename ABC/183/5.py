import copy
H, W = map(int, input().split())
MOD = 10 ** 9 + 7
stage = []
for _ in range(H):
    stage.append(list(input()))
dp = [[0] * W for _ in range(H)]
dp[-1][-1] = 1
sum_val = 1
for i in range(W - 2, -1, -1):
    if stage[H - 1][i] == '#':
        break
    dp[H - 1][i] = sum_val
    sum_val += dp[H - 1][i]
    sum_val %= MOD
sum_val = 1
for i in range(H - 2, -1, -1):
    if stage[i][W - 1] == '#':
        break
    dp[i][W - 1] = sum_val
    sum_val += dp[i][W - 1]
    sum_val %= MOD
# dp_sumの実装
dp_top = copy.deepcopy(dp)
dp_top_left = copy.deepcopy(dp)
dp_left = copy.deepcopy(dp)

for row in range(H - 2, -1, -1):
    for column in range(W - 2, -1, -1):
        if stage[row][column] == '#':
            continue
        dp[row][column] += dp_top[row + 1][column] + dp_left[row][column + 1] + dp_top_left[row + 1][column + 1]
        dp[row][column] %= MOD

        dp_top[row][column] += dp_top[row + 1][column] + dp[row][column]
        dp_top[row][column] %= MOD
        dp_left[row][column] += dp_left[row][column + 1] + dp[row][column]
        dp_left[row][column] %= MOD
        dp_top_left[row][column] += dp_top_left[row + 1][column + 1] + dp[row][column]
        dp_top_left[row][column] %= MOD
'''
print(*dp, sep='\n')
print()
print(*dp_top, sep='\n')
print()
print(*dp_left, sep='\n')
print()
print(*dp_top_left, sep='\n')
'''
print(dp[0][0])