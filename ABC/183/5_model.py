H,W = map(int,input().split())
S = [input() for i in range(H)]
MOD = 10**9+7

dp = [[0]*W for _ in range(H)]
dp[0][0] = 1
cumw = [[0]*(W+1) for _ in range(H)]
cumh = [[0]*W for _ in range(H+1)]
cumd = [[0]*(W+1) for _ in range(H+1)]

for i in range(H):
    for j in range(W):
        if S[i][j]=='#': continue
        if not i==j==0:
            dp[i][j] = cumw[i][j] + cumh[i][j] + cumd[i][j]
            dp[i][j] %= MOD
        cumw[i][j+1] = cumw[i][j] + dp[i][j]
        cumw[i][j+1] %= MOD
        cumh[i+1][j] = cumh[i][j] + dp[i][j]
        cumh[i+1][j] %= MOD
        cumd[i+1][j+1] = cumd[i][j] + dp[i][j]
        cumd[i+1][j+1] %= MOD
print(*dp, sep='\n')
print(dp[-1][-1])