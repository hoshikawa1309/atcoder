H , W = map(int,input().split())
cloud = list(list(input()) for _ in range(H))
stage = [[-1] * W for _ in range(H)]
for row in range(H):
    for column in range(W):
        if cloud[row][column] == "c":
            stage[row][column] = 0

for row in range(H):
    now = 0
    for column in range(W):
        if now == 0 and cloud[row][column] == ".":
            continue
        if cloud[row][column] == "c":
            now = 1
            continue
        stage[row][column] = now
        now += 1
for val in stage:
    print(*val)