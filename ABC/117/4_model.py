n, k = map(int, input().split())
a = list(map(int, input().split()))

# dp[i]: [上からi番目を決定したときの最大値,smaller]
# smaller: {0:次の桁はK以下になるようにする,1:次の桁は何でもok}
dp = [[0, 0] for _ in range(42)]

for i in range(1, 42):
    if dp[i - 1][1] == 1:
        dp[i][1] = 1

    # ctr:i行目が1のAの個数
    ctr = 0
    for j in range(n):
        if (a[j] >> (41 - i)) & 1 == 1:
            ctr += 1

    if ctr >= n - ctr:
        # i行目は0にする
        dp[i][0] = dp[i - 1][0] + ctr * (2 ** (41 - i))
        if (k >> (41 - i)) & 1 == 1:
            dp[i][1] = 1
    else:
        # i行目は1にしたい
        if dp[i][1] == 1:
            # 1にする
            dp[i][0] = dp[i - 1][0] + (n - ctr) * (2 ** (41 - i))
        else:
            if (k >> (41 - i)) & 1 == 1:
                # 1にする
                dp[i][0] = dp[i - 1][0] + (n - ctr) * (2 ** (41 - i))
            else:
                # 1にできないので0にする
                dp[i][0] = dp[i - 1][0] + ctr * (2 ** (41 - i))

print(dp[41][0])
print(dp)