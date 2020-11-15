a, b, c = map(int, input().split())
# if (a + b - c) ** 2 < 4 * a * b:
if 4 * a * b < (c - a - b) ** 2 and c - a - b > 0:
    print('Yes')
else:
    print('No')