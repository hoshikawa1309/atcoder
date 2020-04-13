H, W = map(int, input().split())
canvas = list(list(input()) for _ in range(H))
dx_list = [0, 1, 0, -1]
dy_list = [1, 0, -1, 0]
for x in range(W):
    for y in range(H):
        if canvas[y][x] == ".":
            continue
        is_connect = False
        for dx, dy in zip(dx_list, dy_list):
            if 0 <= x + dx < W and 0 <= y + dy < H:
                if canvas[y + dy][x + dx] == '#':
                    is_connect = True
        if not is_connect:
            print("No")
            exit()
print('Yes')