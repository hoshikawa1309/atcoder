N = int(input())
if N == 1:
    print(0)
    exit()
MOD = 10 ** 9 + 7
all_cnt = pow(10, N, MOD)
zero_include = 1
nine_include = 1
for i in range(1, N):
    zero_include += pow(8, N - i, MOD) * N
    zero_include %= MOD
    nine_include += pow(8, N - i, MOD) * N
    nine_include %= MOD
etc = 8 ** N
ans = all_cnt - zero_include - nine_include - etc
print(ans % MOD)