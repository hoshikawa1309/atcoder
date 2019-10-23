def main():
    import sys
    sys.setrecursionlimit(10 ** 6)
    import sys
    def input():
        return sys.stdin.readline()[:-1]

    H , W = map(int,input().split())
    town = []
    start_x ,start_y = -1 , -1
    for i in range(H):
        wide = list(input())
        if start_y == -1 and start_x == -1:
            for j in range(W):
                if wide[j] == "s":
                    start_x = j
                    start_y = i
        town.append(wide)

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    def dfs(x , y , flag , visited):
        if flag:
            return True
        visited.append([x, y])
        if town[y][x] == "g":
            flag = True
        else:
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if 0 <= next_x and next_x < W and 0 <= next_y and next_y < H and town[next_y][next_x] != "#" and not [next_x,next_y] in visited:
                    flag = dfs(next_x,next_y , flag , visited)
                else:
                    continue
        return flag

    #visited = []
    if dfs(start_x,start_y , False,[]):
        print("Yes")
    else:
        print("No")

main()