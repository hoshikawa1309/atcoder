from math import ceil
N = int(input())
A = list(map(int, input().split()))
if A[0] % 2 == 0 and A[-1] % 2 == 0:
    ans = [min(A[0], A[-1]) * 2]
else:
    ans = [min(A[0], A[-1]) // 2 * 2]

for i in range(N - 1):
    A[i] -= ceil(ans[i] / 2)
    ans.append(A[i] * 2)
print(*ans)