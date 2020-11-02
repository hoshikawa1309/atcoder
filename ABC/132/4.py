import math
def nCk(n, k):
    ret_val = math.factorial(n) // (math.factorial(n - k) * math.factorial(k))
    return ret_val % MOD
N, K = map(int, input().split())
MOD = 10 ** 9 + 7
red_balls = N - K
# 前処理
fact = [0] * (N + 1)
now = 1
for i in range(1, N + 1):
    fact[i] = now
    now *= i
    now %= MOD
print(fact)
print(nCk(6, 4))
for i in range(1, K + 1):
    # ans = math.factorial(red_balls + i) // (math.factorial(red_balls) * math.factorial(i))
    ans = nCk(i + red_balls, red_balls)
    print(ans)
