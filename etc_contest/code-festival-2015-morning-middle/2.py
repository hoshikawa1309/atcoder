def LCS(s1, s2):
    dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
    ret_val = 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[j][i] = dp[j - 1][i - 1] + 1
            else:
                dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])
    return dp[-1][-1]


N = int(input())
s = input()
ans = float('inf')
if N == 1:
    print(1)
    exit()
for i in range(1, N):
    f_s = s[:i]
    l_s = s[i:]
    # print(f_s)
    # print(l_s)
    f_s_len = len(f_s)
    l_s_len = len(l_s)
    common_length = LCS(f_s, l_s)
    ans = min(ans, N - 2 * common_length)
print(ans)