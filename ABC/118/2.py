import numpy as np
N , M = map(int,input().split())
food_list = np.zeros(M)
for i in range(N):
    work = list(map(int,input().split()))
    work.pop(0)
    for idx in work:
        food_list[idx - 1] += 1
cnt = 0
for food in food_list:
    if food == N:
        cnt += 1
print(cnt)