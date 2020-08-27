import copy
N, K = map(int, input().split())
A = list(map(int, input().split()))
routes = [0]
visited = [False] * N
visited[0] = True
now = 0
while True:
    next_town = A[now] - 1
    if visited[next_town]:
        routes.append(next_town)
        break
    visited[next_town] = True
    routes.append(next_town)
    now = next_town
for i, r in enumerate(routes):
    if r == routes[-1]:
        loop = copy.deepcopy(routes[i:])
        break
routes.pop()
loop.pop()
if len(routes) > K:
    print(routes[K] + 1)
else:
    K -= len(routes)
    K %= len(loop)
    print(loop[K] + 1)
