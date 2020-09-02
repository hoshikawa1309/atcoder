import math
A, B, N = map(int, input().split())
x = min(N, B - 1)
print(math.floor((A * x) / B) - A * math.floor(x / B))