import math
x = int(input())
a , f = math.modf(x / 11)
ans = f * 2
#print(f , a)
if a > 0.6:
    ans += 2
elif a > 0:
    ans += 1
print(int(ans))