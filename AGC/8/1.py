x, y = map(int, input().split())
ans = 0
if x <= y:
    if x >= 0 and y >= 0:
        ans = y - x
    elif x < 0 and y < 0:
        ans = abs(x - y)
    else:
        if abs(x) <= y:
            ans = min(y - abs(x) + 1, y - x)
        else:
            ans = min(abs(x) - y + 1, y - x)
else:
    if x >= 0 and y >= 0:
        ans = min(y + x + 1, x - y + 2)
    elif x < 0 and y < 0:
        ans = abs(y - x) + 2
    else:
        if abs(x) <= abs(y):
            ans = abs(y) - x + 1
        else:
            ans = x - abs(y) + 1
print(ans)