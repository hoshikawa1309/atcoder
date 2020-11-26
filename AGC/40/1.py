S = input()
dp = [0] * (len(S) + 1)
for i in range(len(S)):
    if S[i] == '<':
        dp[i + 1] = dp[i] + 1

for i in range(len(S) - 1, -1, -1):
    if S[i] == '>':
        dp[i] = max(dp[i], dp[i + 1] + 1)
print(sum(dp))