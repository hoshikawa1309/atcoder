from collections import deque
from copy import deepcopy
N, K = map(int, input().split())
#V = list(map(int, input().split()))
V = deque(map(int, input().split()))
ans = 0
for l in range(K + 1):
    for r in range(0 , K - l + 1):
        work_V = deepcopy(V)
        if l + r > N:
            continue
        d = K - (r + l)
        now = 0
        hold = []
        for i in range(l):
            #hold.append(V[i])
            hold.append(work_V.popleft())
        for i in range(N - r , N):
            #hold.append(V[-i])
            hold.append(work_V.pop())
        hold.sort()
        now = sum(hold)
        for i in range(d):
            if i >= len(hold):
                break
            if hold[i] > 0:
                break
            else:
                now -= hold[i]
        ans = max(ans , now)
print(ans)