import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

N, M = map(int, input().split())
edge = np.array([input().split() for _ in range(M)], dtype = np.int64).T
print(edge)
print(edge[2])
graph = csr_matrix((edge[2], (edge[:2] - 1)), (N, N))
print(graph)
ans = float('inf')
for i in range(N):
    distance = dijkstra(graph, directed = False, indices = i)
    max_val = np.amax(distance)
    ans = min(ans, max_val)
print(int(ans))