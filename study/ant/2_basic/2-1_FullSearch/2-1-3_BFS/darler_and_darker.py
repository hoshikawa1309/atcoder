from collections import deque
H , W = map(int,input().split())
A = []
start = []
for i in range(H):
    row = list(input())
    for j in range(W):
        if row[j] == "#":
            start.append([i , j])
    A.append(row)

def bfs(s):
    score = [[-1 for _ in range(W)] for _ in range(H)]
    q = deque()
    for y , x in s:
        score[y][x] = 0
        q.append([y,x])
    diff = [[0,1],[1,0],[-1,0],[0,-1]]

    while q:
        now_y , now_x = q.popleft()
        for dy , dx in diff:
            next_y , next_x = now_y + dy , now_x + dx
            if 0 <= next_y and next_y < H and 0 <= next_x and next_x < W and score[next_y][next_x] == -1:
                score[next_y][next_x] = score[now_y][now_x] + 1
                q.append([next_y,next_x])
    ret_val = 0
    for i in range(H):
        for j in range(W):
            ret_val = max(ret_val , score[i][j])
    return ret_val


print(bfs(start))