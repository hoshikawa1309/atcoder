# pypy出だすとmle吐くよ
from collections import deque
H , W = map(int,input().split())
town = tuple(tuple(input()) for _ in range(H))
for i in range(H):
    for j in range(W):
        if town[i][j] == "s":
            sy,sx = i , j
        if town[i][j] == "g":
            gy,gx = i , j
q = deque()
q.append((sy,sx))
cost = [[-1] * W for _ in range(H)]
cost[sy][sx] = 0
diff = ((0,1),(1,0),(0,-1),(-1,0))
while q:
    now_y , now_x = q.popleft()
    for dy , dx in diff:
        next_y , next_x = now_y + dy , now_x + dx
        if 0 <= next_y < H and 0 <= next_x < W and cost[next_y][next_x] == -1:
            if town[next_y][next_x] == "#":
                cost[next_y][next_x] = cost[now_y][now_x] + 1
                q.append((next_y,next_x))
            else:
                cost[next_y][next_x] = cost[now_y][now_x]
                q.appendleft((next_y,next_x))
if cost[gy][gx] < 3:
    print("YES")
else:
    print("NO")

'''
4 5
s####
....#
#####
#...g
'''