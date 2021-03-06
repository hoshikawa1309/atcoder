N, K = map(int, input().split())
# 前処理
triangle = [[0] * 2005 for _ in range(2005)]
triangle[0][0] = 1
MOD = 10 ** 9 + 7
for row in range(2001):
    for column in range(2001):
        if row < column:
            break
        triangle[row + 1][column] += triangle[row][column]
        triangle[row + 1][column] %= MOD
        triangle[row + 1][column + 1] += triangle[row][column]
        triangle[row + 1][column + 1] %= MOD

for i in range(1, K + 1):
    print((triangle[K - 1][i - 1] * triangle[N - K + 1][i]) % MOD)
