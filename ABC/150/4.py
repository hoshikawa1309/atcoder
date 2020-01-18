import math
# 最大公約数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N, M = map(int, input().split())
a = tuple(map(int, input().split()))
tmp = a[0]
lcm_num = tmp
lcm_half = tmp // 2
for i in range(1, N):
    tmp = a[i]
    lcm_num = lcm_num * tmp // gcd(lcm_num, tmp)
    lcm_half = lcm_half * (tmp // 2) // gcd(lcm_half, tmp // 2)
print(math.ceil((M - lcm_half) / lcm_num))