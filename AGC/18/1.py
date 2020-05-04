N, K = map(int, input().split())
A = list(map(int, input().split()))
if K in A:
    print("POSSIBLE")
    exit()
if max(A) < K or N == 1:
    print("IMPOSSIBLE")
    exit()

A.sort()
for i in range(1, N):
    tmp = abs(A[i - 1] - A[i])
    if not tmp == 0 and K % tmp == 0:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
