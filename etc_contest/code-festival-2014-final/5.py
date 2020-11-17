N = int(input())
ans = 0
R = list(map(int, input().split()))
dp = [[0] * N for _ in range(2)]
dp[0][0] = 1
dp[1][0] = 1
for i in range(N - 1):
    if R[i] < R[i + 1]:
        dp[0][i + 1] = dp[1][i] + 1
        dp[1][i + 1] = dp[1][i]
    elif R[i] > R[i + 1]:
        dp[0][i + 1] = dp[0][i]
        dp[1][i + 1] = dp[0][i] + 1
    else:
        dp[0][i + 1] = dp[0][i]
        dp[1][i + 1] = dp[1][i]
# print(dp)
ans = max(dp[0][-1], dp[1][-1])
if ans < 3:
    print(0)
else:
    print(ans)