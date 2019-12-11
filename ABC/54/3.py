N , M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a , b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
visited = [False] * N
visited[0] = True

def dfs(now):
    ans = 0
    visited[now] = True
    #print(visited)
    if all(visited):
        visited[now] = False
        return 1

    for next_node in graph[now]:
        if visited[next_node]:
            continue
        ans += dfs(next_node)
    visited[now] = False
    return ans


print(dfs(0))