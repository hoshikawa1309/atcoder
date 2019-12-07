import sys
sys.setrecursionlimit(10 ** 5)
from functools import lru_cache
N = int(input())

@lru_cache(maxsize=None)
def lucas(n):
    if n <= 1:
        return 2 - n
    else:
        return lucas(n - 2) + lucas(n - 1)

print(lucas(N))