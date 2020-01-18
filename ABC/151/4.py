# 単純にbfsによる探索を行う
# 入力、初期設定など
H, W = map(int,input().split())
maze = list(list(input()) for _ in range(H))
INF = -1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]



def bfs():
    while queue:
        now_row,now_column = queue.pop(0)

        # 上下左右を探索
        # 探索結果が迷路内かつ訪れていないかつ壁でなければvisitedを更新し、そのマスをqueueに追加(いわゆるbfs)
        for i in range(4):
            next_row, next_column = now_row + dy[i] , now_column + dx[i]
            if 0 <= next_row < H and 0 <= next_column < W and \
                    maze[next_row][next_column] != "#" and visited[next_row][next_column] == INF:
                visited[next_row][next_column] = visited[now_row][now_column] + 1
                queue.append([next_row,next_column])


ans = 0
for column in range(W):
    for row in range(H):
        if maze[row][column] == "#":
            continue
        # dequeが使えるかわからないのでリストで代用
        queue = [[row, column]]
        # visitedにはスタートから最短何マスかかるか格納
        visited = [[INF] * W for _ in range(H)]
        visited[row][column] = 0
        bfs()
        tmp_max = 0
        for i in range(H):
            if tmp_max < max(visited[i]):
                tmp_max = max(visited[i])
        if tmp_max > ans:
            ans = tmp_max
print(ans)
