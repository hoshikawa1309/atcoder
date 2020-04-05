N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
sum_A = sum(A)
is_ok = True
for i in range(M):
    check = 1 / (4 * M)
    if A[i] / sum_A < check:
        is_ok = False
        break
print("Yes" if is_ok else "No")