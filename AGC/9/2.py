from collections import deque
N = int(input())
visited = [-1] * N
graph = [[] for _ in range(N)]
for i in range(N - 1):
    x = int(input())
    graph[i + 1].append(x - 1)
    graph[x - 1].append(i + 1)

q = deque([0])
visited[0] = 0
ans = 0
while q:
    now = q.popleft()
    depth = visited[now]
    if now == 0:
        ans = len(graph[0])
    else:
        ans = max(ans, len(graph[now]))
    for next_node in graph[now]:
        if visited[next_node] > -1:
            continue
        visited[next_node] = depth + 1
        q.append(next_node)
# print(visited)
ans = max(ans, max(visited))
print(ans)