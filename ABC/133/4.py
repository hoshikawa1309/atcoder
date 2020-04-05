import numpy as np
N = int(input())
A = list(map(int , input().split()))
'''
#print(A)
b = [sum(A) - 2 * sum(A[1::2])]
print(b)
W = [0] * N
tmp0 = int(np.ceil(A[N-1] / 2) % 2)
tmp1 = int(np.ceil(A[0] / 2) % 2)
if tmp0 == 0 and tmp1 == 0:
    W[0] = int(min(np.ceil(A[N-1] / 2),np.ceil(A[0] / 2)))
elif tmp0 == 0 and tmp1 == 1:
    W[0] = int(np.ceil(A[N-1] / 2))
elif tmp0 == 1 and tmp1 == 0:
    W[0] = int(np.ceil(A[0] / 2))
else:
    W[0] = 0
for i in range(1,N):
    W[i] = 2 * A[i - 1] - W[i - 1]
print(*W)
'''
W = [0] * N
W[0] = sum(A) - 2 * sum(A[1:N - 1:2])

for i in range(1,N):
    W[i] = 2 * A[i - 1] - W[i - 1]
print(*W)