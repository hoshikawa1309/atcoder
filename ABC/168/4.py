from collections import deque
N, M = map(int, input().split())
roads = []
for _ in range(N):
    roads.append([])
for _ in range(M):
    a, b = map(int, input().split())
    roads[a - 1].append(b - 1)
    roads[b - 1].append(a - 1)
visited = [float('inf')] * N
q = deque()
q.append(0)
visited[0] = 0
pre = [-1] * N
while q:
    now_room = q.popleft()
    for next_room in roads[now_room]:
        if visited[next_room] != float('inf'):
            continue
        visited[next_room] = visited[now_room] + 1
        if pre[next_room] == -1:
            pre[next_room] = now_room + 1
        q.append(next_room)
# print(*roads)
# print(*pre)

print('Yes')
for i in range(1, N):
    print(pre[i])
