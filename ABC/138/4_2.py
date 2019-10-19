#from collections import deque
from functools import lru_cache
N , Q = map(int,input().split())
q = []
graph = [[] for _ in range(N)]
point = [0] * N
for _ in range(N - 1):
    a , b = map(int,input().split())
    graph[a - 1].append(b - 1)
for _ in range(Q):
    a , b = map(int,input().split())
    a = a - 1
    point[a] += b
    q.extend(graph[a])
    while q:
        work = q.pop()
        point[work] += b
        q.extend(graph[work])
print(*point)