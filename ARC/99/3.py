import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
'''
one_idx = A.index(1)
before = math.ceil(one_idx / (K - 1))
after = math.ceil((N - one_idx - 1) / (K - 1))
'''
print(math.ceil((N - 1) / (K - 1)))