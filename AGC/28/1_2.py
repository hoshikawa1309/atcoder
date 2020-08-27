import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)


N, M = map(int, input().split())
S = input()
T = input()
L = lcm(N, M)
d = {}
# s = list()
s = set()
for i in range(N):
    d[str(i * (L // N))] = S[i]
    # s.append(str(i * (L // N)))
    s.add(str(i * (L // N)))

for i in range(M):
    key = str(i * (L // M))
    if key in s:
        if d[key] != T[i]:
            print(-1)
            exit()
print(L)