from collections import deque
N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N-1):
    a , b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
visited = [0] * N
visited[0] = 0
#print(tree)
def bfs(now):
    tmp = tree[now]
    tmp.extend([now])
    q = deque([tmp])
    #print(q)
    now_color = visited[now]
    while q:
        next_nodes = q.popleft()
        #print(next_nodes)
        now = next_nodes.pop()
        #print(visited)
        next_color = 0
        for next_node in next_nodes:
            if visited[next_node] == 0 and next_node != 0:
                if next_color + 1 == visited[now]:
                    next_color += 2
                else:
                    next_color += 1
                visited[next_node] = next_color
                tmp = tree[next_node]
                tmp.extend([next_node])
                q.appendleft(tmp)

bfs(0)
print(max(visited))
for i in range(1,len(visited)):
    print(visited[i])