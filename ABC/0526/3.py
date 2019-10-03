import numpy as np
N , M = map(int , input().split())
switch = []
bit_switch = []
for _ in range(M):
    switch = list(map(int ,input().split()))
    del switch[0]
    k = 0
    for i in switch:
        k += 1 << (i - 1)
    bit_switch.append(k)
p = list(map(int,input().split()))
cnt = 0
dp = [[] for _ in range(M + 1)]
dp[0] = [i for i in range(2 ** N)]
print(bit_switch)
print(dp)
for i in range(M):
    for j in dp[i]:
        if str(bin(j & bit_switch[i])).count('1')% 2 == p[i]:
            dp[i + 1].append(j)
print(dp)
print(len(dp[M]))