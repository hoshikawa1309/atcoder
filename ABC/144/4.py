import math
a , b, x = map(int,input().split())

water_h = x / (a ** 2)
emp_high = b - water_h
if 2 * emp_high <= b:
    ans = 2 * emp_high / a
else:
    c = 2 * x / (b * a)
    ans = b / c
print(math.degrees(math.atan(ans)))
