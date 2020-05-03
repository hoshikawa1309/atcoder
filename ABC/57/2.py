N, M = map(int, input().split())
students = [list(map(int,input().split())) for _ in range(N)]
checkpoints = [list(map(int,input().split())) for _ in range(M)]

for x, y in students:
    distance = float('inf')

    for i in range(M):
        gx, gy = checkpoints[i][0], checkpoints[i][1]
        tmp_dis = abs(x - gx) + abs(y - gy)
        if tmp_dis < distance:
            distance = tmp_dis
            ans = i + 1
    print(ans)
