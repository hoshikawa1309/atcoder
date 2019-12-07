N , M = map(int,input().split())
MOD = 10 ** 9 + 7
if abs(N - M) > 1:
    print("0")
    exit()
large = max(N , M)
small = min(N , M)
N_fuct = 1
M_fuct = 1
for i in range(2,large + 1):
    N_fuct *= i
    N_fuct %= MOD
for i in range (2,small + 1):
    M_fuct *= i
    M_fuct %= MOD
ans = N_fuct * M_fuct
if large == small:
    ans *= 2
    print(ans % MOD)
else:
    print(ans % MOD)