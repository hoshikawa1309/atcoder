n = int(input())
a = list(map(int ,input().split()))
A = int(input())
dp = [[0] *(sum(a) + 1) for _ in range(n + 1)]
dp[0][0] = 1
flag = False

for i in range(1, n + 1):
    for j in range(sum(a) + 1):
        dp[i][j] = max(dp[i - 1][j] , dp[i - 1][j - a[i - 1]])
    if dp[i][A] == 1:
        flag = True
        break
if flag:
    print("Yes")
else:
    print("No")