import sys
input = sys.stdin.readline
N , K = map(int,input().split())
h = list(map(int,input().split()))
inf = float('inf')
dp = [inf] * N
if K == 1:
    ans = 0
    for i in range(N - 1):
        ans += abs(h[i + 1] - h[i])
    print(ans)
    exit()

for i in range(N):
    if i == 0:
        min_cost = 0
    elif i == 1:
        min_cost = abs(h[1] - h[0])
    else:
        current = h[i]
        tmp_min = min(abs(current - h[i - K]) + dp[i - K] , abs(current - h[i - K + 1]) + dp[i - K + 1])
        for j in range(K - 2):
            tmp_min = min(abs(current - h[i - K + 2 + j]) + dp[i - K + 2 + j], tmp_min)
        min_cost = tmp_min
    dp[i] = min_cost
#print(dp)
print(dp[N - 1])