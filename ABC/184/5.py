
H, W = map(int, input().split())
stage = [list(input()) for _ in range(H)]
graph = [[] for _ in range(H * W)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
alph_set = set([chr(ord('a') + i) for i in range(26)])
alph_dict = dict()
sr, sc = -1, -1
gr, gc = -1, -1
for i in alph_set:
    alph_dict[i] = list()
for row in range(H):
    for column in range(W):
        for k, l in zip(dx, dy):
            n_row = row + k
            n_column = column + l
            if 0 <= n_row < H and 0 <= n_column < W and stage[n_row][n_column] != '#':
                graph[row * W + column].append((n_row * W + n_column, 1))
        if stage[row][column] in alph_set:
            alph_dict[stage[row][column]].append(row * W + column)
        if stage[row][column] == 'S':
            sr, sc = row, column
            start = row * W + column
        if stage[row][column] == 'G':
            gr, gc = row, column
            goal = row * W + column
for key, val in alph_dict.items():
    if val:
        for i in range(len(val) - 1):
            for j in range(i, len(val)):
                graph[val[i]].append((val[j], 1))
                graph[val[j]].append((val[i], 1))

# print(alph_dict)
# print(graph)

def dijkstra(start, node_cnt, now_graph):
    # start:始点、node_cnt:ノード数、now_graph:隣接グラフ
    import heapq
    INF = float('inf')
    distance = [INF] * node_cnt
    distance[start] = 0
    hq = [[0, start]]
    heapq.heapify(hq)
    seen = [False] * node_cnt
    while hq:
        _, now = heapq.heappop(hq)
        seen[now] = True
        for to, cost in now_graph[now]:
            if not seen[to] and distance[now] + cost < distance[to]:
                distance[to] = distance[now] + cost
                heapq.heappush(hq, list([distance[to], to]))
    return distance





dist = dijkstra(start, H * W, graph)
# print(dist)
if dist[goal] == float('inf'):
    print(-1)
else:
    print(dist[goal])