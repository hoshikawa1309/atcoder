from collections import deque
H, W = map(int, input().split())
sH, sW = map(int, input().split())
sH, sW = sH - 1, sW - 1
gH, gW = map(int, input().split())
gH, gW = gH - 1, gW - 1
graph = []
scores = []
for _ in range(H):
    graph.append(list(input()))
    scores.append([float('inf')] * W)
scores[sH][sW] = 0
q = deque()
m2_q = deque()
q.append([sW, sH])
m2_q.append([sW, sH])
dx_list = [0, 1, 0, -1]
dy_list = [1, 0, -1, 0]
while q or m2_q:
    while q:
        x, y = q.pop()
        for dx, dy in zip(dx_list, dy_list):
            nx, ny = x + dx, y + dy
            if nx < 0 or W <= nx or ny < 0 or H <= ny:
                continue
            if scores[ny][nx] == float('inf') and graph[ny][nx] == '.':
                scores[ny][nx] = scores[y][x]
                q.appendleft([nx, ny])
                m2_q.append([nx, ny])

    while m2_q:
        x, y = m2_q.pop()
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                nx, ny = x + dx, y + dy
                if nx < 0 or W <= nx or ny < 0 or H <= ny:
                    continue

                if scores[ny][nx] > scores[y][x] and graph[ny][nx] == '.':
                    q.append([nx, ny])
                    scores[ny][nx] = scores[y][x] + 1

print(*scores,sep='\n')
if scores[gH][gW] == float('inf'):
    print(-1)
else:
    print(scores[gH][gW])


