import math
H = int(input())
W = int(input())
N = int(input())
target_n = max(H, W)
print(math.ceil(N / target_n))