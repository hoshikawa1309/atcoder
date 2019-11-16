import math
from itertools import permutations
N = int(input())
coodinate = [list(map(int,input().split())) for _ in range(N)]
f_N = math.factorial(N)
SumDistance = 0
j = 0
for val in permutations(coodinate):
    #if j >= math.factorial(N) // 2:
    #    break
    #print(val)
    for i in range(N-1):
        SumDistance += ((val[i+1][0] - val[i][0]) ** 2 + (val[i+1][1] - val[i][1]) ** 2) ** (1 / 2)
    #j += 1

print(SumDistance / math.factorial(N))



