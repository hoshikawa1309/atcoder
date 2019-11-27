from heapq import *
import time
from random import *
import matplotlib.pyplot as plt
time_list = []
cnt_list = []
for i in range(10,1000):
    # 入力
    # V , E = map(int,input().split())
    V = i
    E = randint(i, i * 2)
    graph = []
    for _ in range(E):
        #u, v, a = map(int, input().split())
        u = randint(1, V)
        v = randint(1, V)
        a = randint(1, 100)
        graph.append([u - 1, v - 1,a])
        graph.append([v - 1, u - 1, a])


    # 初期化
    INF = 10**18
    distance = [INF] * V
    distance[0] = 0
    update = True
    start = time.time()
    while update:
        update = False
        for now_node, next_node, add_distance in graph:
            # distanceがINFでなく、次での距離が更新することで短くなるか判定
            if distance[now_node] != INF and distance[next_node] > distance[now_node] + add_distance:
                distance[next_node] = distance[now_node] + add_distance
                update = True
    end = time.time()
    processing_time = end - start
    time_list.append(processing_time)
    cnt_list.append(i)
    #print(distance)
plt.plot(cnt_list,time_list)
plt.show()