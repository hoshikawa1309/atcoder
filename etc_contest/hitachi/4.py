N, T = map(int,input().split())
shops = [list(map(int,input().split())) for _ in range(N)]
ans = 0
shops.sort(reverse=True)
dp = [0] * N
dp[0] = shops[0][0] + shops[0][1]
for i in range(1, N):
    tmp_time = (dp[i - 1] + 1) * shops[i][0] + shops[i][1]
    if 