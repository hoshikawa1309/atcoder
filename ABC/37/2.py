N, Q = map(int, input().split())
A = [0] * N
for _ in range(Q):
    l, r, t = map(int, input().split())
    for i in range(l - 1, r):
        A[i] = t
print(*A, sep='\n')