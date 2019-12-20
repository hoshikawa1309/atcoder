N = int(input())
M = int(input())
target = list(map(int,input().split()))
points = [0] * N
for i in range(M):
    predict = list(map(int,input().split()))
    now_target = target[i]
    for j in range(N):
        if now_target == predict[j]:
            points[j] += 1
        else:
            points[now_target - 1] += 1
for val in points:
    print(val)