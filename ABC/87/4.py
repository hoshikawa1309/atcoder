from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    l, r, d = map(int, input().split())
    graph[l - 1].append([r - 1, d])
    graph[r - 1].append([l - 1, -d])

INF = float('inf')
dis_list = [INF] * N
for now in range(N):
    if dis_list[now] != INF:
        continue
    dis_list[now] = 0
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        for next_node, distance in graph[now]:
            if dis_list[next_node] == INF:
                dis_list[next_node] = dis_list[now] + distance
                q.append(next_node)
            else:
                if dis_list[next_node] != dis_list[now] + distance:
                    print('No')
                    exit()
# print(dis_list)
print('Yes')