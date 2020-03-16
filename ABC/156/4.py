N, a, b = map(int,input().split())
cmb = [N]
mod = MOD = 10**9+7

# for i in range(1 , max(a,b) + 1):
#     cmb.append(cmb[-1] * (N - i) % mod // (i + 1))
print(cmb)

def nCr(n,r):
    res=1
    fac=1
    for i in range(r):
        res *= n-i
        res %= MOD
        fac *= i+1
        fac %= MOD
    return res*pow(fac, MOD-2, MOD)%MOD


print((pow(2, N,mod) - nCr(N, a) - nCr(N, b) - 1) % mod)