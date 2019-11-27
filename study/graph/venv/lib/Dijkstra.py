from heapq import *
import time
from random import *
import matplotlib.pyplot as plt
time_list = []
cnt_list = []
# 入力
for i in range(10,1000):
    # n , m = map(int,input().split())
    n = i
    m = randint(i,i * 2)
    cost1 = [[] for _ in range(n)]
    for _ in range(m):
        #u, v, a = map(int, input().split())
        u = randint(1,n)
        v = randint(1,n)
        a = randint(1,100)
        cost1[u - 1].append((v - 1, a))
        cost1[v - 1].append((u - 1, a))

    start = time.time()
    def dijkstra(cost , N , start):
        # 初期化
        INF = float('inf')
        distance = [INF] * N
        distance[start] = 0
        previous = [-1] * N
        q = []
        # heapqを用いてるため、自動的に最短が出力
        heappush(q , (0,start))
        while q:
            now = heappop(q)[1]
            #現在のノードから次のノードとそこへの距離を探索
            for next_node , next_distance in cost[now]:
                # 次のノードに行けるとき
                if next_distance < INF:
                    sum_distance = distance[now] + next_distance
                    # 次のノードまでの距離の総和が現在調べたものより短いとき更新を行う
                    if distance[next_node] > sum_distance:
                        distance[next_node] = sum_distance
                        previous[next_node] = now
                        heappush(q , (distance[next_node],next_node))
        return distance
    d1 = dijkstra(cost1,n,0)
    end = time.time()
    processing_time = end - start
    time_list.append(processing_time)
    cnt_list.append(i)
    #print(d1)
    #print("{}[sec]".format(processing_time))
plt.plot(cnt_list,time_list)
plt.show()