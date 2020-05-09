import sys

input = sys.stdin.readline
from collections import *


def dfs(now):
    if len(now) == N:
        print(''.join(now))
        return

    M = max(now)

    for i in range(ord(M) - ord('a') + 2):
        now.append(alpha[i])
        dfs(now)
        now.pop()


N = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
dfs(deque(['a']))