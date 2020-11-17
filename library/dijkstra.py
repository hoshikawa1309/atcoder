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


if __name__ == '__main__':
    # ノード数, エッジ数, 始点ノード
    v, e, r = map(int, input().split())
    # adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
    adj = [[] for _ in range(v)]
    for i in range(e):
        s, t, d = map(int, input().split())
        adj[s].append((t, d))
    print(dijkstra(0, v, adj))

    '''
    入力例
    4 5 0 # ノード数, エッジ数, 始点ノード
    0 1 1
    0 2 4
    1 2 2
    2 3 1
    1 3 5
    '''