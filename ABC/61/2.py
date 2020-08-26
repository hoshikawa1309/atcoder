N, M = map(int, input().split())
road = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    road[a - 1] += 1
    road[b - 1] += 1
print(*road, sep='\n')