#from collections import deque
from functools import lru_cache
N , Q = map(int,input().split())
stack = []
graph = [[] for _ in range(N)]
point = [0] * N
for _ in range(N - 1):
    a , b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
for _ in range(Q):
    a , b = map(int,input().split())
    a = a - 1
    point[a] += b

def dfs(now , prev = -1):
    for next in graph[now]:
        if next == prev:
            continue
        print(now , next)
        print(point)
        point[next] += point[now]
        dfs(next , now)

print(point)
dfs(0)
print(*point)
'''
    q.extend(graph[a])
    while q:
        work = q.pop()
        point[work] += b
        q.extend(graph[work])
print(*point)
'''