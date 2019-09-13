import heapq
N , M = map(int , input().split())
jobs = [list(map(int , input().split())) for _ in range(N)]
jobs.sort()

q = []
index = 0
ans = 0
for limit in range(1 , M + 1):
    while index < N:
        time =jobs[index][0]
        reward = jobs[index][1]
        if limit >= time:
            heapq.heappush(q , -reward)
            index += 1
        else:
            break
    print(q)
    if len(q) != 0:
        tmp = heapq.heappop(q)
        ans -= tmp

print(ans)
