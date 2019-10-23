from copy import deepcopy
from pprint import pprint
import sys
sys.setrecursionlimit(10 ** 6)
island = [list(input()) for _ in range(10)]
island_cnt = 0
for val in island:
    island_cnt += val.count("o")
island_cnt += 1
#print(island_cnt)
for i in range(10):
    for j in range(10):
        if island[i][j] == "o":
            start_row, start_column = i , j
            break
    if island[i][j] == "o":
        break

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(land_fill_island ,column , row , cnt):
    print(cnt)
    if visited[row][column] or column < 0 or column >= 10 or row < 0 or row >= 10 or land_fill_island[row][column] == "x":
        return
    else:
        if cnt == island_cnt:
            print("Yes")
            exit()
        visited[row][column] = True
        for i in range(4):
            dfs(land_fill_island,column + dx[i] , row + dy[i],cnt + 1)


for i in range(10):
    for j in range(10):
        if island[i][j] == "o":
            continue
        visited = [[False] * 10 for _ in range(10)]
        work_island = deepcopy(island)
        work_island[i][j] = "o"
        print(i , j)
        pprint(work_island)
        dfs(work_island ,start_column , start_row,1)
print("No")
