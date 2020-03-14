a, b, c = map(int, input().split())
if c - a - b > 0 and 4 * a * b < (c - a - b) ** 2:
    print("Yes")
else:
    print("No")