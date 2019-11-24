from collections import deque
N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N-1):
    a , b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
visited = [0] * N
visited[0] = 1
print(tree)
def bfs(now):
    q = deque([tree[now]])
    now_color = visited[now]
    while q:
        tmp = q.pop()
        for next_node in tmp:
            print(next_node)
            if visited[next_node] == 0:
                visited[next_node] = now_color + 1
                q.appendleft(tree[next_node])

bfs(0)
print(visited)
for i in visited:
    print(i)