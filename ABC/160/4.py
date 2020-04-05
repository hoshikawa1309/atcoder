# 入力
N, X, Y = map(int, input().split())
Graph = [[] for _ in range(N)]
for i in range(N):
    if i < N - 1:
        Graph[i].append(i + 1)
        Graph[i + 1].append(i)
    if X == i:
        Graph[X - 1].append(Y - 1)
        Graph[Y - 1].append(X - 1)
# print(Graph)


ans = [0] * (N - 1)
from collections import deque

# 全ての点からDFSを行い、最短距離を求める
for i in range(N):
    dist = [-1]*N
    que = deque([i])
    dist[i] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in Graph[v]:
            if dist[w] > -1:
                continue
            dist[w] = d + 1
            que.append(w)
    # print(dist)

    # 最短距離の個数をansに格納する
    for d in dist:
        if d > 0:
            ans[d - 1] += 1

# 全ての点からの最短距離を格納した。
# 条件1 <= i < j <= Nより、1 => 2はカウントするが、2 => 1はカウントしない。
# そのため、2で割って帳尻合わせを行う。
for a in ans:
    print(a // 2)
