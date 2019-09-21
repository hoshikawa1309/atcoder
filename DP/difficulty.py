MOD = 10 ** 9 + 7
# from functools import lru_cache
from bisect import bisect_left

N = int(input())
D = [int(input()) for _ in range(N)]
D.sort()

if D[0] * 8 > D[-1]:
    print(0)
    exit()

nx = [-1] * N
for index, d in enumerate(D):
    print(d)
    j = bisect_left(D, d * 2)
    nx[index] = j
#print(nx)
dp = [1] * N
for _ in range(3):
    cum = [0] * N
    for index, x in enumerate(dp):
        j = nx[index]
        if j == N:
            break
        cum[j] += x
    for i in range(N - 1):
        cum[i + 1] += cum[i]
        cum[i + 1] %= MOD

    dp = cum
    print(dp)
#print(dp)
ans = 0
for i in dp:
    ans += i
    ans %= MOD

print(ans)