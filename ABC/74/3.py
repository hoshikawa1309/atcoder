import sys
sys.setrecursionlimit(10 ** 6)
from functools import lru_cache
A, B, C, D, E, F = map(int, input().split())

amount_of_water = [False] * (F + 1)
dp = [[0] * (F + 1) for _ in range(F + 1)]
def rec(n):
    if n > F:
        return
    amount_of_water[n] = True
    rec(n + 100 * A)
    rec(n + 100 * B)
rec(0)

@lru_cache(maxsize=None)
def rec_sugar(water, sugar):
    concentration = sugar / (water + sugar)
    if water + sugar > F or concentration > E / (100 + E):
        return
    dp[water][sugar] = concentration
    rec_sugar(water, sugar + C)
    rec_sugar(water, sugar + D)


for i in range(1, F + 1):
    if amount_of_water[i]:
        rec_sugar(i, 0)

ans = 0
ans_sugar = 0
ans_water = 0
for i in range(F + 1):
    for j in range(F + 1):
        if dp[i][j] > ans:
            ans_water = i
            ans_sugar = j
            ans = dp[i][j]
# print(ans)
if ans == 0:
    print(min(100 * A, 100 * B), 0)
else:
    print(ans_water + ans_sugar, ans_sugar)