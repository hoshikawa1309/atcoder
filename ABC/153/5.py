from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 6)
Hitpoint, N = map(int, input().split())
magic_damage = []
magic_point = []
for _ in range(N):
    A, B = map(int, input().split())
    magic_damage.append(A)
    magic_point.append(B)

# dp = [[float("inf") for _ in range(Hitpoint + 1)] for _ in range(N + 1)]
dp = [float('inf') for _ in range(Hitpoint + 1)]
dp[0] = 0
for i in range(N):
    for now_HP in range(Hitpoint + 1):
        next_HP = min(now_HP + magic_damage[i], Hitpoint)
        dp[next_HP] = min(dp[next_HP], dp[now_HP] + magic_point[i])
        # dp[i + 1][now_HP] = min(dp[i + 1][now_HP], dp[i][now_HP - magic_damage[i]] + magic_point[i])
print(dp[Hitpoint])


'''
@lru_cache(maxsize=None)
def solve(i, now_HP):
    if now_HP <= 0:
        retval = 0
    elif i == N:
        retval = float('inf')
    else:
        if now_HP <= magic_damage[i]:
            retval = min(solve(i + 1, now_HP),
                         solve(i + 1, now_HP - magic_damage[i]) + magic_point[i])
        else:
            retval = min(solve(i + 1, now_HP),
                         solve(i + 1, now_HP % magic_damage[i]) + magic_point[i] * (now_HP // magic_damage[i]))
    return retval


print(solve(0, Hitpoint))
'''
