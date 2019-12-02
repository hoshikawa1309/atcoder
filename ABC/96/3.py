H , W = map(int,input().split())
stage = list(list(input()) for _ in range(H))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
for i in range(H):
    for j in range(W):
        if stage[i][j] == ".":
            continue
        Flag = True
        for k in range(4):
            if 0 <= j + dx[k] < W and 0 <= i + dy[k] < H and stage[i + dy[k]][j + dx[k]] == "#":
                Flag = False
                break
        if Flag:
            print("No")
            exit()
print("Yes")
