import heapq
import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
logs = []
heapq.heapify(logs)
for a in A:
    heapq.heappush(logs, [-a, -a, 1])


for _ in range(K):
    log = heapq.heappop(logs)
    dividing_equal = log[2] + 1
    cut_log = log[1] / dividing_equal
    origin_log = log[1]

    heapq.heappush(logs, [cut_log, origin_log, dividing_equal])
print(math.ceil(-logs[0][0]))