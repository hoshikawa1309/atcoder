#from pprint import pprint
N = int(input())
points = list(map(int,input().split()))
dp = [[False] * (sum(points) + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(N):
    for j in range(sum(points)):
        if dp[i][j]:
            dp[i + 1][j + points[i]] = dp[i+1][j] = True
#pprint(dp)
print(dp[N].count(True))