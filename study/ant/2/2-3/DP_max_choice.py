n = int(input())
a = list(map(int , input().split()))
print(a)
dp = [0] * (len(a) + 1)
for i in range(0,n):
    dp[i + 1] = max(dp[i] , dp[i] + a[i - 1])
print(max(dp))