N = int(input())
h = list(map(int,input().split()))
inf = float('inf')
dp = [0] + [abs(h[1] - h[0])]+ [inf] * (N - 2)
for i in range(2 , N):
    dp[i] = min(abs(h[i] - h[i - 2]) + dp[i - 2], abs(h[i - 1] - h[i]) + dp[i - 1])
print(dp)
print(dp[N - 1])