import sys
sys.setrecursionlimit(10 ** 5)
N , K = map(int,input().split())
T = list(list(map(int,input().split())) for _ in range(N))
def dfs(idx , now):
    if idx == N:
        return now == 0
    for val in T[idx]:
        if dfs(idx + 1,now ^ val):
            return True
    return False

print("Found" if dfs(0,0) else "Nothing")