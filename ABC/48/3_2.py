N, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
sum_val = A[0] + A[1]
if A[0] + A[1] > x:
    if A[1] >= sum_val - x:
        ans += sum_val - x
        A[1] -= sum_val - x
    else:
        ans += A[1] + (A[0] - x)
        A[0] -= (x - A[1])
        A[1] = 0
# print(A)
# print(ans)

for i in range(1, N - 1):
    sum_val = A[i] + A[i + 1]
    if sum_val <= x:
        continue
    ans += sum_val - x
    A[i + 1] -= sum_val - x
# print(A)
print(ans)