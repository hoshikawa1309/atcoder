N = int(input())
graph = []
for _ in range(N):
    x, y = map(int, input().split())
    graph.append([x, y])
if N == 1:
    print(1)
    exit()
ans = float('inf')
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        p = graph[i][0] - graph[j][0]
        q = graph[i][1] - graph[j][1]
        vec_cnt = 0
        for k in range(N):
            for l in range(N):
                if p == graph[k][0] - graph[l][0] and q == graph[k][1] - graph[l][1]:
                    vec_cnt += 1
        ans = min(ans, N - vec_cnt)
print(ans)