H, W = map(int, input().split())
graph = []
cnt = []
for _ in range(H):
    graph.append(list(input()))
    cnt.append([0] * W)

if graph[0][0] == '#':
    cnt[0][0] = 1
else:
    cnt[0][0] = 0

for i in range(H - 1):
    for j in range(W - 1):
        if i == j == 0:
            continue
        if graph[i][j] == '.' and graph[i + 1][j] == '#':
            graph[i + 1][j] = graph[i][j] + 1
        elif graph[i][j] == '.' and graph[i][j + 1] == '#':
            graph[i + 1][j + 1] = graph[i][j] + 1
        else:
            graph[i + 1][j + 1] = graph[i][j]
            graph[i + 1][j + 1] = graph[i][j]