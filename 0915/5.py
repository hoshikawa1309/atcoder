'''
N = int(input())
S = input()
ans = 0
for i in range(N // 2):
    for j in range(i + 1, N):
        str = S[i:j]
        search = S[j:]
        print(search[:i + 1])
        if str == search[:i + 1]:
            ans = len(str)
print(ans)
'''
from pprint import pprint
#N  = int(input())
S1 = input()
S2 = input()
dp = [[0] * (len(S1) + 1)] * (len(S2) + 1)
pprint(dp[0][0])
print(len(S1))
for i in range(len(S1)):
    for j in range(len(S2)):
        if S1[i] == S2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1] , dp[i+1][j])
        pprint(dp)
pprint(dp)
print(dp[len(S1)][len(S2)])
