N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    xi, yi = points[i]
    for j in range(N):
        if i == j:
            continue
        xj, yj = points[j]
        for k in range(N):
            if i == k or j == k:
                continue
            xk, yk = points[k]
            # if (dxij + dxjk == dxik and dyij + dxjk == dxik) or (dxij + dxik == dyjk and dyij + dyik == dyjk) or (dxik + dxjk == dxij and dyik + dyjk == dyij):
            if (yi - yj) * (xk - xi) == (yk - yi) * (xi - xj):
                print('Yes')
                exit()
print('No')