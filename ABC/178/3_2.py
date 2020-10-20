N = int(input())
MOD = 10 ** 9 + 7
print((pow(10, N, MOD) - (pow(9, N, MOD) + pow(9, N, MOD) - pow(8, N, MOD) )) % MOD)