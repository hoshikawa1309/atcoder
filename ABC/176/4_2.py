from collections import deque
H, W = map(int, input().split())
sH, sW = map(int, input().split())
sH, sW = sH - 1, sW - 1
gH, gW = map(int, input().split())
gH, gW = gH - 1, gW - 1
stage = []
scores = []
for _ in range(H):
    stage.append(list(input()))
    scores.append([float('inf')] * W)
scores[sH][sW] = 0
moveA_q = deque()
moveB_q = deque()
moveA_q.append([sW, sH])
moveB_q.append([sW, sH])
dx_list = [0, 1, 0, -1]
dy_list = [1, 0, -1, 0]
while moveA_q or moveB_q:
    if scores[gH][gW] != float('inf'):
        break
    # 移動AでBFS
    while moveA_q:
        x, y = moveA_q.pop()
        # ここ
        # moveB_q.append([x, y])

        for dx, dy in zip(dx_list, dy_list):
            nx, ny = x + dx, y + dy
            if nx < 0 or W <= nx or ny < 0 or H <= ny or stage[ny][nx] == '#':
                continue
            # if scores[ny][nx] == float('inf'):
            if scores[ny][nx] > scores[y][x]:
                scores[ny][nx] = scores[y][x]
                moveA_q.append([nx, ny])
                # ここ
                moveB_q.append([nx, ny])


    # 移動bで動けるマスをmodeA_qに格納
    while moveB_q:
        x, y = moveB_q.pop()
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                nx, ny = x + dx, y + dy
                if nx < 0 or W <= nx or ny < 0 or H <= ny or stage[ny][nx] == '#':
                    continue
                # if scores[ny][nx] == float('inf'):
                if scores[ny][nx] > scores[y][x]:
                    moveA_q.append([nx, ny])
                    scores[ny][nx] = scores[y][x] + 1

print(*scores,sep='\n')
if scores[gH][gW] == float('inf'):
    print(-1)
else:
    print(scores[gH][gW])
