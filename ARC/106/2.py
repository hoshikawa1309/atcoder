
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
'''
N, M = 2 * 10 ** 5, 0
A = [10 ** 9] * N
B = [10 ** 9] * N
'''
graph = [[] for _ in range(N)]
for i in range(M):
    c, d = map(int, input().split())
    graph[c - 1].append(d - 1)
    graph[d - 1].append(c - 1)

for i in range(N):
    a_sum = A[i]
    b_sum = B[i]
    if not graph[i]:
        continue
    for node in graph[i]:
        a_sum += A[node]
        b_sum += B[node]
    if a_sum != b_sum:
        print('No')
        exit()
    for node in graph[i]:
        if node == i:
            continue
        graph[node].clear()
    graph[i].clear()
print('Yes')