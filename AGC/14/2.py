N, M = map(int, input().split())
A = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    A[a] += 1
    A[b] += 1
if all([i % 2 == 0 for i in A]):
    print('YES')
else:
    print('NO')