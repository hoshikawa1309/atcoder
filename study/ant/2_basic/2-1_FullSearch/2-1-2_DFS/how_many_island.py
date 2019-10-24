import sys
sys.setrecursionlimit(10 ** 6)
islands = []
visited_list = []
w_list = []
h_list = []
while True:
    w ,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    w_list.append(w)
    h_list.append(h)
    island = [list(input().split()) for _ in range(h)]
    islands.append(island)
    visited_list.append([[False] * w for _ in range(h)])

dx = [0,1,1, 1, 0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1, 0, 1]

def dfs(island_m ,now_row , now_column , idx):
    if now_row < 0 or h_list[idx] <= now_row or now_column < 0 or w_list[idx] <= now_column or island_m[now_row][now_column] == "0":
        return
    if visited_list[idx][now_row][now_column]:
        return
    visited_list[idx][now_row][now_column] = True
    for i in range(8):
        dfs(island_m,now_row + dx[i] ,now_column + dy[i],idx)


for m in range(len(islands)):
    cnt = 0
    for row in range(h_list[m]):
        for column in range(w_list[m]):
            if not visited_list[m][row][column] and islands[m][row][column] == "1":
                dfs(islands[m] , row , column , m)
                cnt += 1
    print(cnt)