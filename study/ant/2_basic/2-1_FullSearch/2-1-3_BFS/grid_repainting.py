from collections import deque

H , W = map(int,input().split())
maze = []
white_cnt = -1
for _ in range(H):
    row = list(input())
    white_cnt += row.count(".")
    maze.append(row)

def bfs(sy,sx,gy,gx , ma):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    score = [[-1 for _ in range(W)] for _ in range(H)]
    score[sy][sx] = 0
    q = deque()
    q.append([sy,sx])
    while q:
        now_y , now_x = q.popleft()
        for i in range(4):
            next_y , next_x = now_y + dy[i] , now_x + dx[i]
            if 0 <= next_y and next_y < H and 0 <= next_x and next_x < W and score[next_y][next_x] == -1 and ma[next_y][next_x] == ".":
                q.append([next_y,next_x])
                score[next_y][next_x] = score[now_y][now_x] + 1
    return score[gy][gx]


min_distance = bfs(0 , 0,H - 1,W - 1 , maze)
if min_distance == -1:
    print(min_distance)
else:
    print(white_cnt - min_distance)