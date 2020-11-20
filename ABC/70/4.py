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


N = int(input())
graph =[[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))
Q, K = map(int, input().split())
dist = dijkstra(K - 1, N, graph)
for _ in range(Q):
    x, y = map(int, input().split())
    print(dist[x - 1] + dist[y - 1])