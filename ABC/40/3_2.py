N = int(input())
posts = list(map(int, input().split()))
dp = [0] * N
dp[1] = abs(posts[0] - posts[1])
for i in range(2, N):
    dp[i] = min(abs(posts[i] - posts[i - 1]) + dp[i - 1], abs(posts[i] - posts[i - 2]) + dp[i - 2])
print(dp[-1])