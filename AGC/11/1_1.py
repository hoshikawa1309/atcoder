from collections import deque
N, C, K = map(int, input().split())
times = []
for _ in range(N):
    time = int(input())
    times.append(time)
times.sort()
times = deque(times)
ans = 0
bus_time = times[0] + K
human = 0
while times:
    if times[0] <= bus_time:
        times.popleft()
        human += 1
        if human == C:
            ans += 1
            human = 0
            if times:
               bus_time = times[0] + K
    else:
        human = 0
        ans += 1
        bus_time = times[0] + K
if human:
    print(ans + 1)
else:
    print(ans)