import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


N = int(input())
ans = int(input())
for _ in range(N - 1):
    ans = lcm(ans, int(input()))
print(ans)