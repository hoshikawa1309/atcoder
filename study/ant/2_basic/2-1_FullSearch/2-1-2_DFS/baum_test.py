import sys
sys.setrecursionlimit(10 ** 6)
N , M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u , v = map(int,input().split())
    u , v = u - 1 , v - 1
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * N

def dfs(now , parent):
    visited[now] = True
    for next_node in graph[now]:
        if next_node == parent:
            continue
        if visited[next_node]:
            return False
        if not dfs(next_node , now):
            return False
    return True


cnt = 0
for i in range(N):
    if visited[i]:
        continue
    f = dfs(i , -1)
    if f:
        cnt += 1
print(cnt)