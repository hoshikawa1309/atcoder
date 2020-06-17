import numpy as np
N , M , C = map(int,input().split())
B = np.array(list(map(int,input().split())))
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))
A = np.array(A)
cnt = 0

for i in range(N):
    if sum(A[i] * B) + C > 0:
        cnt += 1
print(cnt)