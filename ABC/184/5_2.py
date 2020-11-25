from collections import deque
H, W = map(int, input().split())
stage = [input() for _ in range(H)]
INF = float('inf')
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
alph_dict = [[] for _ in range(26)]

for row in range(H):
    for column in range(W):
        if stage[row][column].islower():
            alph_dict[ord(stage[row][column]) - 97].append((row, column))
        if stage[row][column] == 'S':
            sr, sc = row, column
        if stage[row][column] == 'G':
            gr, gc = row, column

dist = [[INF] * W for _ in range(H)]
dist[sr][sc] = 0
q = deque()
q.append((sr, sc))

while q:
    row, column = q.popleft()
    next_cost = dist[row][column] + 1
    for i in range(4):
        n_row = row + dy[i]
        n_column = column + dx[i]
        # 通常のBFS
        if n_row < 0 or H <= n_row or n_column < 0 or W <= n_column or stage[n_row][n_column] == '#':
            continue
        if dist[n_row][n_column] > next_cost:
            dist[n_row][n_column] = next_cost
            q.append((n_row, n_column))

        # アルファベットのワープをqに追加する
        if stage[row][column].islower():
            alph_idx = ord(stage[row][column]) - 97
            for warp_row, warp_column in alph_dict[alph_idx]:
                if dist[warp_row][warp_column] > next_cost:
                    dist[warp_row][warp_column] = next_cost
                    q.append((warp_row, warp_column))
            alph_dict[alph_idx].clear()

ans = -1 if dist[gr][gc] == INF else dist[gr][gc]
print(ans)