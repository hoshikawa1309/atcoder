N = int(input())
edge = []
if N % 2 == 0:
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            if i == j:
                continue
            if j == N - i + 1:
                continue
            edge.append([i, j])
else:
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            if i == j:
                continue
            if N - i == j:
                continue
            edge.append([i, j])
print(len(edge))
for e in edge:
    print(*e)