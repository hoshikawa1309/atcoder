from collections import deque
H , W = map(int,input().split())
town = []
for i in range(H):
    row = list(input())
    for j in range(W):
        if row[j] == "s":
            sy,sx = i , j
        if row[j] == "g":
            gy,gx = i , j
    town.append(row)

def dfs(sy,sx,gy,gx):
    q = deque()
    q.append([sy,sx])
    possible = [[False for _ in range(W)] for _ in range(W)]
    possible[sy][sx] = True
    diff = [[0,1],[1,0],[0,-1],[-1,0]]
    connect_dim = [[0,-3],[1,-2],[2,-1],[3,0],[2,1],[1,2],[0,3],[-1,2],[-2,1],[-3,0],[-2,-1],[-2,-1],]
    while q:
        now_y , now_x = q.popleft()
        for dy , dx in diff:
            next_y , next_x = now_y + dy , now_x + dx
            if 0 <= next_y and next_y < H and 0 <= next_x and next_x < W and possible[next_y][next_x] == False and town[next_y][next_x] == ".":
                possible[next_y][next_x] = True
                q.append([next_y,next_x])

    q.append([gy,gx])
    while q:
        now_y , now_x = q.popleft()
        for dy, dx in connect_dim:
            next_y, next_x = now_y + dy,now_x + dx
            if 0 <= next_y and next_y < H and 0 <= next_x and next_x < W and possible[next_y][next_x] == True:
                return True
        for dy , dx in diff:
            next_y , next_x = now_y + dy , now_x + dx
            if 0 <= next_y and next_y < H and 0 <= next_x and next_x < W and possible[next_y][next_x] == False and town[next_y][next_x] == ".":
                possible[next_y][next_x] = True
                q.append([next_y,next_x])
    return False





if dfs(sy,sx,gy,gx):
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