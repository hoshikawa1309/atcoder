N = int(input())
A = list(map(int ,input().split()))

cnt = 0
for i in range(N):
    if A[i] < 0:
        cnt += 1
        A[i] = -1 * A[i]
if cnt % 2 == 0:
    print(sum(A))
else:
    A.sort()
    print(sum(A) - A[0] * 2)