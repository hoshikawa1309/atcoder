N = int(input())
a = list(map(int,input().split()))
dp = [0] * N
dp[1] = abs(a[0] - a[1])
for i in range(2,N):
    dp[i] = min(dp[i - 2] + abs(a[i - 2] - a[i]) , dp[i - 1] + abs(a[i - 1] - a[i]))
print(dp[N - 1])