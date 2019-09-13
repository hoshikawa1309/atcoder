N , M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a , b = map(int , input().split())
    #print(a , b)
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

ans = []
for i in range(N):
    count = []
    friend = graph[i]
    for j in friend:
        for k in graph[j]:
            if k not in graph[i] and k != i:
                count.append(k)
    #print(count)
    print(len(set(count)))
