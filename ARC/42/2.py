import numpy as np

init_x, init_y = map(int, input().split())
N = int(input())
ans = float('inf')
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append([x, y])
points.append(points[0])
# print(points)
for idx in range(N):
    x1, y1 = points[idx]
    x2, y2 = points[idx + 1]
    u = np.array([x1 - x2, y1 - y2])
    v = np.array([init_x - x2, init_y - y2])
    tmp_ans = abs(np.cross(u, v) / np.linalg.norm(u))
    # print(tmp_ans)
    ans = min(tmp_ans, ans)
print(ans)