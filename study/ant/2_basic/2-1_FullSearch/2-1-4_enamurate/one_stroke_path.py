import sys
sys.setrecursionlimit(10**5)
N , M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a , b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

visited = [False] * N
ans = 0
def dfs(now):
    global ans
    if all(visited):
        ans += 1
    for next_node in graph[now]:
        if visited[next_node] is False:
            visited[next_node] = True
            dfs(next_node)
            visited[next_node] = False

visited[0] = True
dfs(0)
print(ans)