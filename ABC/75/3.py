# 方針: N本のそれぞれを抜いた時全ての頂点を探索することができるか判定し、カウントを行う。
import copy
N , M = map(int,input().split())

tmp_list = []
for _ in range(M):
    a , b = map(int,input().split())
    tmp_list.append([a - 1,b - 1])

def dfs(now):
    stack = [work_graph[now]]
    while stack:
        next_nodes = stack.pop()
        for next_node in next_nodes:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(work_graph[next_node])


cnt = 0
for i in range(M):
    work_graph = [[] for _ in range(N)]
    for j in range(M):
        if j == i:
            continue
        work_graph[tmp_list[j][0]].append(tmp_list[j][1])
        work_graph[tmp_list[j][1]].append(tmp_list[j][0])
    visited = [False] * N
    dfs(0)
    if not all(visited):
        cnt += 1
print(cnt)

