from operator import mul
from functools import reduce
MOD = 10**9+7


def nCr(n,r):
    res=1
    fac=1
    for i in range(r):
        res *= n-i
        res %= MOD
        fac *= i+1
        fac %= MOD
    print('res', res)
    print('fac', fac)
    return res*pow(fac, MOD-2, MOD) % MOD

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under % MOD
print(nCr(10**9, 10**5))
print(pow(10**9, 10**5, 10**9+7))
# print(cmb(10**9, 10**5))