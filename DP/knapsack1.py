'''遅い
import sys

input = sys.stdin.readline
N, W = map(int, input().split())
weight = []
value = []
for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)


def knapsack():
    dp = [[-1] * (W + 1) for _ in range(N + 1)]

    def solve(i, w):
        if dp[i][w] != -1:
            return dp[i][w]
        if N == i:
            ret_val = 0
        elif w - weight[i] < 0:
            ret_val = solve(i + 1, w)
        else:
            ret_val = max(solve(i + 1, w), solve(i + 1, w - weight[i]) + value[i])
        dp[i][w] = ret_val
        return dp[i][w]

    solve(0, W)
    # print(dp)
    return max(dp[0])


if __name__ == "__main__":
    print(knapsack())
'''

import numpy as np
N , W = map(int, input().split())
goods = np.array([list(map(int , input().split())) for _ in range(N)])
dp = np.zeros((N + 1 , W + 1) , dtype = np.int)

for i in range(0,N):
    w, v = goods[i,:]
    dp[i + 1, w:] = np.maximum(dp[i,w:] , dp[i,:-w] + v)
    dp[i + 1, :] = np.maximum(dp[i + 1,:],dp[i,:])
print(int(dp[N,W]))