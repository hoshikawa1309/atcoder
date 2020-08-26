K = int(input())
now = 1
ans = 7
mod = 10 ** 9 + 7
for i in range(K + 1):
    if ans % K == 0:
        print(now)
        exit()
    now += 1
    # ans += 7 * 10 ** (i + 1)
    # ans %= 10 ** 9 + 7
    # ans += 7 * 10 ** (i + 1) % mod
    ans += 7 * pow(10, i + 1, K) % K


print('-1')