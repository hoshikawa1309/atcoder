import numpy as np
N = int(input())
time = np.array([int(input()) for _ in range(5)])
place = np.zeros(6)
place[0] = N
end = 0
cnt = 0
'''
while place[5] != N:

    cnt += 1
    for i in range(4,-1,-1):
        now = place[i + 1]
        work = min(place[i] , time[i])
        place[i + 1] += work
        place[i] -= work
    #print(place)
'''
ans = 0
min_val = min(time)
print(int(np.ceil(N / min_val) + 4))
'''
for i in range(len(time)):
    if min > time[i]:
        min = time[i]
    ans += np.ceil(N / min) + i
'''

