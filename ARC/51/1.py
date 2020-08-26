x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())
if x1 + r <= x3 and x2 <= x1 - r and y1 + r <= y3 and y2 <= y1 - r:
    print('NO')
else:
    print('YES')

if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r ** 2 and (x3 - x1) ** 2 + (y3 - y1) ** 2 <= r ** 2 and (x2 - x1) ** 2 + (y3 - y1) ** 2 <= r ** 2 and (x3 - x1) ** 2 + (y2 - y1) ** 2 <= r ** 2:
    print('NO')
else:
    print('YES')
