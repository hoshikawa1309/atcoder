# パスカルの三角形を用いて、組み合わせの計算を行う。
# modを取ってるので注意
def nCk(n, k):
    return triangle[n][k]

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

