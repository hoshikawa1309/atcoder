import math
arms = list(map(int, input().split()))
OA, AB, BC = arms[0], arms[1], arms[2]
arms.sort()
max_r = sum(arms)
max_area = max_r * max_r * math.pi
if arms[2] <= arms[1] + arms[0]:
    print(max_area)
else:
    min_r = min(abs(OA + AB - BC), abs(OA - AB - BC), abs(OA - AB + BC))
    print(max_area - min_r * min_r * math.pi)