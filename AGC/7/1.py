H, W = map(int, input().split())
A = []
flags = []
for _ in range(H):
    A.append(list(input()))
    flags.append([False] * W)
x, y = 0, 0
flags[0][0] = True
while True:
    nx1, ny1 = x + 0, y + 1
    nx2, ny2 = x + 1, y + 0
    if x == W - 1 and y == H - 1:
        break
    if x == W - 1:
        if A[ny1][nx1] == '#':
            x, y = nx1, ny1
        else:
            print('Impossible')
            exit()
    elif y == H - 1:
        if A[ny2][nx2] == '#':
            x, y = nx2, ny2
        else:
            print('Impossible')
            exit()
    else:
        if A[ny1][nx1] == '#' and A[ny2][nx2] == '.':
            x, y = nx1, ny1
        elif A[ny1][nx1] == '.' and A[ny2][nx2] == '#':
            x, y = nx2, ny2
        else:
            print('Impossible')
            exit()
    flags[y][x] = True
# print(*flags, sep='\n')
for x in range(W):
    for y in range(H):
        if A[y][x] == '#' and not flags[y][x]:
            print('Impossible')
            exit()
print('Possible')