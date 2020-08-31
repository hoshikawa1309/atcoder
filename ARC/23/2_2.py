r, c, d = map(int, input().split())
stage = []
for _ in range(r):
    stage.append(list(map(int, input().split())))

ans = 0
for y in range(r):
    for x in range(c):
        if (y + x) <= d and (y + x) % 2 == (d % 2):
            ans = max(ans, stage[y][x])
print(ans)
