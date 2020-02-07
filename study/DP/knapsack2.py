'''
N, W = map(int, input().split())
weight = []
value = []
for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)
value_sum = sum(value)
dp = []
for _ in range(N + 1):
    dp_val = [float('inf') for _ in range(value_sum + 1)]
    dp.append(dp_val)
dp[0][0] = 0

for idx in range(N):
    for v in range(value_sum + 1):
        if value[idx] <= v:
            dp[idx + 1][v] = min(dp[idx][v], dp[idx][v - value[idx]] + weight[idx])
        else:
            dp[idx + 1][v] = dp[idx][v]
ans = 0
# print(dp)
for i in range(value_sum + 1):
    if dp[-1][i] <= W:
        ans = i
print(ans)

'''

import numpy as np
N, W = map(int, input().split())
weight = []
value = []
for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)
value_sum = sum(value)
dp = [[float('inf') for _ in range(value_sum + 1)] for _ in range(N + 1)]
dp = np.full((N + 1, value_sum + 1), float('inf'))
dp[0][0] = 0
# print(dp)
for idx in range(N):
    for v in range(value_sum + 1):
        if value[idx] <= v:
            dp[idx + 1][v] = min(dp[idx][v], dp[idx][v - value[idx]] + weight[idx])
        else:
            dp[idx + 1][v] = dp[idx][v]
ans = 0
# print(dp)
for i in range(value_sum + 1):
    if dp[N][i] <= W:
        ans = i
print(ans)
