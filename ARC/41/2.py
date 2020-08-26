N, M = map(int, input().split())
stage = []
ans = []
for _ in range(N):
    row = list(map(lambda x: int(x), input()))
    stage.append(row)
    ans.append([0] * M)
move = [[0, 0], [-1, 1], [1, 1], [0, 2]]
for y in range(N):
    for x in range(M):
        if stage[y][x] > 0:
            cnt = stage[y][x]
            ans[y + 1][x] = stage[y][x]
            for dx, dy in move:
                stage[y + dy][x + dx] -= cnt
for row in ans:
    print(*row, sep='')