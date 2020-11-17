H, W = map(int, input().split())
stage = [list(map(int, input().split())) for _ in range(H)]
ans = []
for y in range(H):
    row = stage[y]
    if y == 0:
        for x in range(W - 1):
            if row[x] % 2 == 1:
                ans.append([y + 1, x + 1, y + 1, x + 2])
                row[x + 1] += 1
        if y == H - 1:
            break
        if row[-1] % 2 == 1:
            ans.append([y + 1, W, y + 2, W])
            stage[y + 1][-1] += 1
    else:
        for x in range(W - 1, 0, -1):
            if row[x] % 2 == 1:
                ans.append([y + 1, x + 1, y + 1, x])
                row[x - 1] += 1
        if y == H - 1:
            break
        if row[0] % 2 == 1:
            ans.append([y + 1, 1, y + 2, 1])
            stage[y + 1][0] += 1
print(len(ans))
if len(ans):
    for a in ans:
        print(*a)