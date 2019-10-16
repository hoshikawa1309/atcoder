# 頂点sから到達する頂点の集合
def dfs(edge, s):
    use = {s}
    q = [s]
    while q:
        v = q.pop()
        for w in edge[v]:
            if w in use:continue
            use.add(w)
            q.append(w)
    return use

# ベルマンフォード法
def bellman_ford(v, s, t, e):
    INF = 10**18
    # コストをINFで初期化
    d = [INF] * v
    # 開始頂点は0
    d[s] = 0
    # 負の閉路が無ければ更新はV-1回までで終わる
    for _ in range(v):
        f = False
        for a, b, c in e:
            if d[a]==INF:continue
            # aまでのコスト+辺abのコストがbまでのコストより小さければ更新
            cost = d[a] + c
            if cost < d[b]:
                d[b] = cost
                f = True
        # 更新が無ければbreak
        if not f:break
    else:
        # V回目まで更新があったら負の閉路がある
        return -1
    return max(-d[t], 0)

def main():
    import sys
    input = sys.stdin.readline
    n, m, p = map(int, input().split())
    edge = [[] for _ in range(n)]
    edge_rev = [[] for _ in range(n)]
    e = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge[a-1].append(b-1)
        # 頂点Nからdfsするため辺の向きを逆にする
        edge_rev[b-1].append(a-1)
        e.append((a-1, b-1, p-c))
    """
    # 頂点1と頂点Nのどちらからも到達できる頂点の集合
    use = dfs(edge, 0) & dfs(edge_rev, n-1)
    # fromとtoがどちらもuseに含まれる辺のみ使う
    # そうすることで負の閉路を検出した場合答えは必ず-1になる
    """
    # ↑って思ってたけど頂点Nから到達できるか見るだけでいいらしいよ(えー)
    use = dfs(edge_rev, n-1)
    e = [(a, b, c) for a, b, c in e if a in use and b in use]
    print(bellman_ford(n, 0, n-1, e))
if __name__ == '__main__':
    main()
