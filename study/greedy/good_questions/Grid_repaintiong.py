from collections import deque

def dfs(stage , visited , start_x,start_y,goal_x,goal_y):
    queue = deque([[start_x,start_y]])
    visited[start_x][start_y] = 1
    while queue:
        x , y = queue.popleft()
        if [x , y] == [goal_x,goal_y]:
            return visited[x][y]

        for dx , dy in ([1,0],[-1,0],[0,1],[0,-1]):
            new_x , new_y = x + dx , dy + y
            #print(new_x,new_y)
            if 0 <= new_x <= goal_x and 0 <= new_y <= goal_y  and stage[new_x][new_y] == "." and visited[new_x][new_y] == -1:
                #print(new_x , new_y)
                visited[new_x][new_y] = visited[x][y] + 1
                queue.append([new_x,new_y])
    print("-1")
    exit(0)
if __name__ == "__main__":
    H , W = map(int , input().split())
    stage = []
    for _ in range(H):
        stage.append(list(input()))
    start_x,start_y ,goal_x,goal_y = 0,0,H-1,W-1
    visited = [[-1] * W for _ in range(H)]
    #print(visited)
    #print(stage)
    #print(visited[0][1])
    sum = 0
    for value in stage:
        sum += value.count('.')
    #print(sum)
    print(sum - dfs(stage,visited,start_x,start_y,goal_x,goal_y))
