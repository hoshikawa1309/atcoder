import math
x, y, a, b = map(int, input().split())
ans = 0
while x * a < x + b and x < y:
    x *= a
    ans += 1
if x != y - 1:
    ans += (y - x - 1) // b
print(ans)