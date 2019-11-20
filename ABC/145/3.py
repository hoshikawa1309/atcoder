import math
from itertools import permutations
N = int(input())
coodinate = [list(map(int,input().split())) for _ in range(N)]
SumDistance = 0
for val in permutations(coodinate):
    for i in range(len(val) - 1):
        SumDistance += ((val[i+1][0] - val[i][0]) ** 2 + (val[i+1][1] - val[i][1]) ** 2) ** (1 / 2)
print(SumDistance / math.factorial(N))


import numpy as np
import math
from itertools import permutations
N = int(input())
coodinate = [list(map(int,input().split())) for _ in range(N)]
coodinate = np.array(coodinate)
SumDistance = 0
for val in permutations(coodinate):
    for i in range(N-1):
        SumDistance += ((val[i+1][0] - val[i][0]) ** 2 + (val[i+1][1] - val[i][1]) ** 2) ** (1 / 2)
print(SumDistance / math.factorial(N))
