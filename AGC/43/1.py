from collections import deque
H, W = map(int, input().split())
# H, W = 100, 100
maze = []
for _ in range(H):
    maze.append(list(input()))
    # maze.append(['#'] * W)
costs = []
for _ in range(H):
    costs.append([float('inf')] * W)
if maze[0][0] == '.':
    costs[0][0] = 0
else:
    costs[0][0] = 1
dx_list = [0, 1]
dy_list = [1, 0]
q = deque()
q.append([0, 0])

while q:
    x, y = q.popleft()
    if x == W - 1 and y == H - 1:
        break
    for dx, dy in zip(dx_list, dy_list):
        next_x = x + dx
        next_y = y + dy
        if 0 <= next_x <= W - 1 and 0 <= next_y <= H - 1 and costs[next_y][next_x] == float('inf'):
            if maze[next_y][next_x] == '#':
                costs[next_y][next_x] = min(costs[y][x] + 1, costs[next_y][next_x])
                q.append([next_x, next_y])
            else:
                costs[next_y][next_x] = min(costs[y][x], costs[next_y][next_x])
                q.appendleft([next_x, next_y])
# print(*costs, sep='\n')
print(costs[-1][-1])

