N = int(input())
distance = []
population = []
coordinate = []
for _ in range(N):
    x, y, p = map(int, input().split())
    coordinate.append([x, y])
    distance.append(min(abs(x), abs(y)))
    population.append(p)

