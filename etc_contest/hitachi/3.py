from collections import deque
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

print(graph)
visited = [False] * N
for i in range(N):
    visited = [False] * N
    stack = deque()
    stack.append(graph[i])
    visited[i] = True
    for j in range(3):
        cnt = len(stack)
        for _ in range(cnt):
            next_nodes = stack.pop()
            for next_node in next_nodes:
                if visited[next_node]:
                    continue
                visited[next_node] = True
                stack.append(graph[next_node])
    print(stack)