H , W = map(int,input().split())
stage = list(input() for _ in range(H))
dy_list = [1,1,0,-1,-1,-1,0,1]
dx_list = [0,1,1,1,0,-1,-1,-1]

for y in range(H):
    for x in range(W):
        cnt = 0
        Flag = False
        for dx , dy in zip(dy_list , dx_list):
            if stage[y][x] == "#":
                break
            Flag = True
            if 0 <= y + dy < H and 0 <= x + dx < W:
                if stage[y + dy][x + dx] == "#":
                    cnt += 1
        if Flag:
            print(cnt , end = "")
        else:
            print("#" ,end = "")
    print()