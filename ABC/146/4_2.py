from collections import deque
# 入力、初期化
N = int(input())
tree = [[] for _ in range(N)]
input_list = []
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    input_list.append([a, b])
    tree[a].append(b)
    tree[b].append(a)


# visitedにノードの色を格納する
# visited_edge = [[0] * N for _ in range(N)]
dict = {}
'''
# bfsによる色付けを行う
def bfs(now_node, max_val=0):
    queue = deque([[tree[now_node], -1, now_node]])
    while queue:
        next_nodes, before_color, now_node = queue.pop()
        now_color = 1
        for next_node in next_nodes:
            if visited_edge[now_node][next_node] != 0:
                continue
            if now_color == before_color:
                now_color += 1
            if max_val < now_color:
                max_val = now_color
            visited_edge[next_node][now_node] = now_color
            visited_edge[now_node][next_node] = now_color
            queue.appendleft([tree[next_node], now_color, next_node])
            now_color += 1
    return max_val
'''
def bfs(now_node, max_val=0):
    queue = deque([[tree[now_node], -1, now_node]])
    while queue:
        next_nodes, before_color, now_node = queue.pop()
        now_color = 1
        for next_node in next_nodes:
            key = tuple(sorted([now_node, next_node]))
            if not dict.get(key) is None:
                continue
            if now_color == before_color:
                now_color += 1
            if max_val < now_color:
                max_val = now_color
            dict[key] = now_color
            # visited_edge[now_node][next_node] = now_color
            queue.appendleft([tree[next_node], now_color, next_node])
            now_color += 1
    return max_val

ans = bfs(0)
print(ans)
for a, b in input_list:
    # print(visited_edge[a][b])
    print(dict[tuple(sorted([a,b]))])
