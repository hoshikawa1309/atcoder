N = int(input())
cities = []
for _ in range(N):
    now = list(map(int, input().split()))
    cities.append(now)

dist = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        dist[i][j] = abs(cities[j][0] - cities[i][0]) + abs(cities[j][1] - cities[i][1]) + max(0, cities[j][2] - cities[i][2])

INF = float('inf')
dp = [[float('inf')] * (N) for _ in range(2 ** N )]
dp[1][0] = 0

for i in range(2 ** N):
    for j in range(N):
        if dp[i][j] == INF:
            continue
        for k in range(N):
            if (i >> k) % 2 == 1:
                continue
            next_i = i | (2 ** k)
            next_d = dp[i][j] + dist[j][k]
            dp[next_i][k] = min(dp[next_i][k], next_d)

all_v = 2 ** N - 1
ans = INF
for i in range(N):
    if dp[all_v][i] == INF:
        continue
    tmp = dp[all_v][i] + dist[i][0]
    ans = min(ans, tmp)
print(ans)

print(*dp, sep='\n')
