from heapq import *
import time
from random import *
import matplotlib.pyplot as plt
time_list = []
cnt_list = []
def warshall_floyd(distance):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                distance[i][j] = min(distance[i][j] , distance[i][k] + distance[k][j])
    return distance

for i in range(10,100):
    #n , m = map(int,input().split())
    n = i
    m = randint(i,i * 2)
    INF = float('inf')
    cost1 = [[INF for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        #u , v , a = map(int,input().split())
        u = randint(1, n)
        v = randint(1, n)
        a = randint(1, 100)
        cost1[u-1][v-1] = a
        cost1[v-1][u-1] = a
    start = time.time()
    d = warshall_floyd(cost1)
    end = time.time()
    processing_time = end - start
    time_list.append(processing_time)
    cnt_list.append(i)
plt.plot(cnt_list,time_list)
plt.show()
