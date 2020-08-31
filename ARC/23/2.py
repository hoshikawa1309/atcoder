from collections import deque
r, c, d = map(int, input().split())
stage = []
cnt_list = []
for _ in range(r):
    stage.append(list(map(int, input().split())))
    cnt_list.append([-1] * c)
cnt_list[0][0] = 0
q = deque()
q.append([0,0])
diff = [[0, 1], [1, 0]]
while q:
    y, x = q.popleft()
    for dx, dy in diff:
        nx = dx + x
        ny = dy + y
        if r <= ny or c <= nx or cnt_list[ny][nx] != -1:
            continue
        cnt_list[ny][nx] = cnt_list[y][x] + 1
        q.append([ny, nx])

ans = 0
for y in range(r):
    for x in range(c):
        if cnt_list[y][x] <= d and cnt_list[y][x] % 2 == d % 2:
            ans = max(ans, stage[y][x])
print(ans)