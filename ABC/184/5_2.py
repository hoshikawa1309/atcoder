from collections import deque
H, W = map(int, input().split())
# H, W = 2000, 2000
stage = [list(input()) for _ in range(H)]
# stage = [['a'] * W for _ in range(H)]
# stage[0][0] = 'S'
# stage[-1][-1] = 'G'
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
alph_set = set([chr(ord('a') + i) for i in range(26)])
alph_visited = [False] * 26
alph_dict = dict()
sr, sc = -1, -1
gr, gc = -1, -1
for i in alph_set:
    alph_dict[i] = set()
for row in range(H):
    for column in range(W):
        if stage[row][column] in alph_set:
            alph_dict[stage[row][column]].add((row, column))
        if stage[row][column] == 'S':
            sr, sc = row, column
        if stage[row][column] == 'G':
            gr, gc = row, column

dist = [[float('inf')] * W for _ in range(H)]
dist[sr][sc] = 0
q = deque()
q.append((sr, sc))

while q:
    row, column = q.popleft()
    for k, l in zip(dx, dy):
        n_row = row + k
        n_column = column + l
        # 通常のBFS
        if 0 <= n_row < H and 0 <= n_column < W and stage[n_row][n_column] != '#' and dist[n_row][n_column] == float('inf'):
            dist[n_row][n_column] = dist[row][column] + 1
            q.append((n_row, n_column))

        # アルファベットのワープをqに追加する
        c = stage[row][column]
        if c in alph_set and not alph_visited[ord(c) - 97]:
            warp_grid = alph_dict[c]
            for warp_row, warp_column in warp_grid:
                if dist[warp_row][warp_column] == float('inf'):
                    dist[warp_row][warp_column] = dist[row][column] + 1
                    q.append((warp_row, warp_column))
            alph_visited[ord(c) - 97] = True

if dist[gr][gc] == float('inf'):
    print(-1)
else:
    print(dist[gr][gc])