import math
import itertools
N, K = map(int, input().split())
towns = [i for i in range(N)]
Times = list(list(map(int, input().split())) for _ in range(N))
ans = 0
for path in itertools.permutations(towns):
    if path[0] != 0:
        break
    sum_val = 0
    for i in range(N - 1):
        sum_val += Times[path[i]][path[i + 1]]
    sum_val += Times[path[-1]][0]
    if sum_val == K:
        ans += 1
print(ans)