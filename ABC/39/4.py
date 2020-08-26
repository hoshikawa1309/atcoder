H, W = map(int, input().split())
stage = []
after = []
restore = []
for _ in range(H):
    stage.append(list(input()))
    after.append(['.'] * W)
    restore.append(['.'] * W)
for h in range(H):
    for w in range(W):
        flag = True
        for k in range(-1, 2):
            for l in range(-1, 2):
                nh = h + k
                nw = w + l
                if 0 <= nh < H and 0 <= nw < W and stage[nh][nw] == '.':
                    flag = False
        if flag:
            after[h][w] = '#'

# print(*after, sep='\n')
for h in range(H):
    for w in range(W):
        if after[h][w] == '.':
            continue
        for k in range(-1, 2):
            for l in range(-1, 2):
                nh = h + k
                nw = w + l
                if 0 <= nh < H and 0 <= nw < W:
                    restore[nh][nw] = '#'
# print(*restore, sep='\n')
if restore == stage:
    print('possible')
    for row in after:
        print(*row, sep='')
else:
    print('impossible')