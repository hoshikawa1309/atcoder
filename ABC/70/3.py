import math
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(x, y):
    return (x * y) // gcd(x, y)

N = int(input())
T = [int(input()) for _ in range(N)]
if N == 1:
    print(T[0])
    exit()

ans = lcm(T[0] , T[1])
for i in range(2 , N):
    ans = lcm(T[i] , ans)
print(ans)