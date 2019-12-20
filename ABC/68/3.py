N , M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a , b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

for node0 in graph[0]:
    for node1 in graph[node0]:
        if node1 == N - 1:
            print("POSSIBLE")
            exit()
print("IMPOSSIBLE")