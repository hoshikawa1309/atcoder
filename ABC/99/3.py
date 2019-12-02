import sys
sys.setrecursionlimit(10**6)
from functools import lru_cache

@lru_cache(maxsize=None)
def solve(val , now):
    if val < 6 or now == 0:
        ret_val = val
    # 何もしない
    elif val < counts[now]:
        ret_val = solve(val , now - 1)
    # 何もしない or 手を加えるの小さい方
    else:
        ret_val = min(solve(val , now - 1) , solve(val - counts[now] , now) + 1)
    return ret_val

N = int(input())
coins = [1,6,9]
counts = [1]
for i in range(1,3):
    for j in range(1,N):
        if coins[i] ** j <= N:
            counts.append(coins[i] ** j)
        else:
            break
#print(counts)
print(solve(N , len(counts) - 1))