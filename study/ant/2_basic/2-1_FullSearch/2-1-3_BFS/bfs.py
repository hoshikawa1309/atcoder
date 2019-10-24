from collections import deque
R , C = map(int,input().split())
sy , sx = map(int,input().split())
sy , sx = sy - 1 , sx - 1
gy , gx = map(int,input().split())
gy , gx = gy - 1 , gx - 1

maze = [list(input()) for _ in range(R)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(y , x , cnt):
    visited = [[y , x]]
    q = deque()
    q.append([y , x])
    while q:
        yx = q.popleft()
        cnt += 1
        for i in range(0 , len(yx) , 2):
            now_y, now_x = yx[i] ,yx[i + 1]
            for i in range(4):
                next_y = now_y + dy[i]
                next_x = now_x + dx[i]
                if next_x < 0 or C <= next_x or next_y < 0 or R <= next_y or [next_y , next_x] in visited:
                    continue
                if maze[next_y][next_x] == "#":
                    continue
                if next_y == gy and next_x == gx:
                    return cnt
                if q:
                    q[0].extend([next_y , next_x])
                else:
                    q.append([next_y,next_x])
                visited.append([next_y , next_x])
    return cnt


ans = dfs(sy , sx , 0)
print(ans)
