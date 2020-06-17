import numpy as np
N , K = map(int,input().split())
ans = 0
for i in range(1 , N + 1):
    j = i
    idx = 0
    while j < K:
        j *= 2
        idx += 1
    ans += 1 / N * np.power(1 / 2 , idx)
print(ans)