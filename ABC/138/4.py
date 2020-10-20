from collections import deque
N, Q = map(int, input().split())
tree = [[] for _ in range(N)]
visited = [False] * N
visited[0] = True
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

ans = [0] * N
points = [0] * N

for _ in range(Q):
    p, x = map(int, input().split())
    points[p - 1] += x

now_point = 0
stack = deque()
stack.append([0, points[0]])
while stack:
    now_node, now_point = stack.popleft()
    ans[now_node] = now_point
    for next_node in tree[now_node]:
        if visited[next_node]:
            continue
        visited[next_node] = True
        stack.append([next_node, now_point + points[next_node]])
print(*ans)