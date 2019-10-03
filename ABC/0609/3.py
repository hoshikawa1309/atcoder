''' ansの値が大きくなりすぎてエラー
from functools import lru_cache
import sys

sys.setrecursionlimit(10**5)
N , M = map(int ,input().split())
mod = 10 ** 9 + 7
A = []
for i in range(M):
    A.append(int(input()))
    if A[i] - 1 == A[i - 1] and i > 0:
        print("0")
        exit()
@lru_cache(maxsize=None)
def fib(n):
    if memo[n] != 0:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1)+fib(n - 2)
ans = 1
now = 0
for a in A:
    next = a - 1
    ans *= fib(next - now)
    now = a + 1
if now == 0:
    ans = fib(N)
else:
    ans *= fib(N - now)
print(ans % mod)
'''

N , M = map(int ,input().split())
mod = 10 ** 9 + 7
A = []
crash = 0
idx = 0
for i in range(M):
    A.append(int(input()))
    if i == 0:
        crash = A[0]
    if A[i] - 1 == A[i - 1] and i > 0:
        print("0")
        exit()
dp = [0] * (N + 1)
dp[0] = 1

for i in range(1 , N + 1):
    if i == crash:
        idx += 1
        if idx < M:
            crash = A[idx]
    else:
        if i == 1:
            dp[1] = 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= mod
print(dp[-1])
