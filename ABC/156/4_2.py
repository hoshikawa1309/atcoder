def nCk(N, K):
    MOD = 10 ** 9 + 7
    ret_val = 1
    for i in range(K):
        ret_val *= (N - i)
        ret_val //= (i + 1)
        ret_val %= MOD
    return ret_val % MOD


n, a, b = map(int, input().split())
MOD = 10 ** 9 + 7
all_cnt = pow(2, n, MOD) - 1
a_cnt = nCk(n, a)
b_cnt = nCk(n, b)
ans = all_cnt - a_cnt - b_cnt
while ans < 0:
    ans += 10 ** 9 + 7
print(ans)

