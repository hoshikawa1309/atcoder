
S = input()
#S = "?" * 100000
S = S[::-1]
N = 13
mod = 10 ** 9 + 7
dp = [0] * 26
dp[13] = 1
digit = 1
for c in range(len(S)):
    dp[:13] = [0] * N
    if S[c] == '?':
        for k in range(10):
            for j in range(N):
                dp[(k * digit + j) % N] += dp[j + 13]
                dp[(k * digit + j) % N] %= mod
    else:
        k = int(S[c])
        for j in range(N):
            #index = (k * digit + j) % N
            dp[(k * digit + j) % N] += dp[j + 13]
            dp[(k * digit + j) % N] %= mod

    digit *= 10
    digit %= N
    #print(dp)
    dp[13:26] = dp[:13]
    #print(dp)
print(dp[5])
'''

r = [[(j - k) * 9 % 13 for j in range(10)] for k in range(13)]
d = [1] + [0] * 12
M = 10 ** 9 + 7
for c in input():
    if c == '?':
        d = [sum(d[j] for j in k) % M for k in r]
    else:
        d = [d[(int(c) - k) * 9 % 13] for k in range(13)]
    #print(d)
print(d[5])
'''