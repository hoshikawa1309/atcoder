A, B, C = map(int, input().split())
MOD = 998244353
sigma_A = (A * (A + 1)) // 2
sigma_A %= MOD
sigma_B = (B * (B + 1)) // 2
sigma_B %= MOD
sigma_C = (C * (C + 1)) // 2
sigma_C %= MOD
print((sigma_A * sigma_B * sigma_C) % MOD)