from collections import deque
H, W = map(int, input().split())
sH, sW = map(int, input().split())
sH, sW = sH - 1, sW - 1
gH, gW = map(int, input().split())
gH, gW = gH - 1, gW - 1
stage = []
costs = []
for _ in range(H):
    stage.append(list(input()))
    costs.append([float('inf')] * W)
costs[sH][sW] = 0
move_q = deque()
move_q.append([sW, sH, 0])
dx_list = [0, 1, 0, -1]
dy_list = [1, 0, -1, 0]
while move_q:
    # 移動AでBFS
    x, y, now_cost = move_q.pop()
    for dx, dy in zip(dx_list, dy_list):
        nx, ny = x + dx, y + dy
        if nx < 0 or W <= nx or ny < 0 or H <= ny or stage[ny][nx] == '#':
            continue
        if costs[ny][nx] > now_cost:
            costs[ny][nx] = now_cost
            move_q.appendleft([nx, ny, now_cost])

    # 移動bで動けるマスをmodeA_qに格納
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            nx, ny = x + dx, y + dy
            if nx < 0 or W <= nx or ny < 0 or H <= ny or stage[ny][nx] == '#':
                continue
            # if costs[ny][nx] == float('inf'):
            if costs[ny][nx] > now_cost:
                costs[ny][nx] = now_cost + 1
                move_q.append([nx, ny])


# print(*costs,sep='\n')
if costs[gH][gW] == float('inf'):
    print(-1)
else:
    print(costs[gH][gW])
