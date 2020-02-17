#N = input()[::-1]
N = input()
len_N = len(N)
ans = 0
next_bit = False

for i in range(len_N):
    tmp = int(N[i])
    # dp[i] = min(10 - tmp + 1 + dp[i - 1], dp[i - 1] + tmp)
    if tmp > 5:
        if next_bit:
            ans += 10 - tmp
        else:
            ans += 10 - tmp + 1
            next_bit = True
    else:
        if next_bit:
            next_bit = False
        ans += tmp


print(ans)
