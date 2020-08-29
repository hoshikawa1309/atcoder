def modinv(a, m):
    b = m
    u = 1
    v = 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m
    if u < 0:
        u += m
    return u

def nCk(N, k, mod):
    ret_val = 1
    for i in range(k):
        ret_val *= (N - i)
        ret_val %= mod
        ret_val *= modinv(i + 1, mod)
        ret_val %= mod
    return ret_val


n, a, b = map(int, input().split())
MOD = 10 ** 9 + 7
all_cnt = pow(2, n, MOD) - 1
a_cnt = nCk(n, a, MOD)
b_cnt = nCk(n, b, MOD)
ans = all_cnt - a_cnt - b_cnt
while ans < 0:
    ans += MOD
print(ans)
