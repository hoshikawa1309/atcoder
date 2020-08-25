H, W = map(int, input().split())
stage = []
scores = []
for _ in range(H):
    stage.append(list(input()))
    scores.append([float('inf')] * W)
if stage[0][0] == '#':
    scores[0][0] = 1
else:
    scores[0][0] = 0
move = [[0, 1], [1, 0]]
for y in range(H):
    for x in range(W):
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if H <= ny or W <= nx:
                continue
            if stage[ny][nx] == '#' and stage[y][x] == '.':
                scores[ny][nx] = min(scores[ny][nx], scores[y][x] + 1)
            else:
                scores[ny][nx] = min(scores[ny][nx], scores[y][x])
# print(*scores, sep='\n')
print(scores[-1][-1])