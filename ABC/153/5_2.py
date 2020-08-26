import math
H, N = map(int, input().split())
dp = [[0 for _ in range(H + 1)] for _ in range(N)]
A, B = map(int, input().split())
for i in range(H + 1):
    cnt = math.ceil(i / A)
    dp[0][i] = B * cnt

for i in range(1, N):
    A, B = map(int, input().split())
    for j in range(H + 1):
        dp[i][j] = min(dp[i - 1][j], dp[i][max(j - A, 0)] + B)
# print(*dp, sep='\n')
print(dp[-1][-1])