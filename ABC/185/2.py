N, M, T = map(int, input().split())
now = 0
max_charge = N
for _ in range(M):
    A, B = map(int, input().split())
    N -= A - now
    if N <= 0:
        print('No')
        exit()
    N = min(N + B - A, max_charge)
    now = B
if T - now < N:
    print('Yes')
else:
    print('No')