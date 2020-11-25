N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if N < M:
    print('NO')
    exit()
A.sort(reverse=True)
B.sort(reverse=True)

for i in range(M):
    a = A[i]
    b = B[i]
    if a < b:
        print('NO')
        exit()
print('YES')