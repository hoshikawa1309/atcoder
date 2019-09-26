import numpy as np
s = input()
t = input()
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1] , dp[i][j] + 1)
        dp[i+1][j+1] = max(dp[i][j+1] , dp[i+1][j] ,dp[i+1][j+1])
print(dp)
dp = np.array(dp).T
for i in range(1,len(s) + 1):
    if dp[len(t)][i] != dp[len(t)][i - 1]:
        print(s[i-1] , end = '')