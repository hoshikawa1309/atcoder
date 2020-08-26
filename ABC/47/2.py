import numpy as np
from pprint import pprint
W, H, N = map(int, input().split())
area = np.ones((H, W))
# pprint(area[1][:3])
for _ in range(N):
    x, y, a = map(int, input().split())
    y = H - y
    if a == 1:
        for i in range(H):
            area[i][:x] = 0
    elif a == 2:
        for i in range(H):
            area[i][x:] = 0
    elif a == 3:
        for i in range(y, H):
            area[i] = 0
    elif a == 4:
        for i in range(y):
            area[i] = 0
pprint(int(area.sum()))