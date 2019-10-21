import sys
sys.setrecursionlimit(10 ** 6)
N , Q = map(int,input().split())
graph = [[] for _ in range(N)]
point = [0] * N
for _ in range(N - 1):
    a , b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
#print(graph)
for _ in range(Q):
    a , b = map(int,input().split())
    a = a - 1
    point[a] += b

# dfsを用いて累積和を計算する
# 初期状態だと前の値がないためデフォルト引数に-1を代入
def dfs(now , prev = -1):
    for next in graph[now]:
        # 次のノードが前に参照した値の時はcontinue
        if next == prev:
            continue

        # 現在の値を次のポイントに加算することで累積和をとる
        point[next] += point[now]

        # 次のノードと現在のノードを引数にdfsを継続する
        dfs(next , now)

dfs(0)
print(*point)