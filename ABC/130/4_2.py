import bisect
N, K = map(int, input().split())
A = list(map(int, input().split()))
A_sum = [0] * (N + 1)
for idx, a in enumerate(A):
    A_sum[idx + 1] = A_sum[idx] + a
# print(A_sum)

ans = 0
for a in A_sum:
    idx = bisect.bisect_left(A_sum, K + a)
    ans += N - idx + 1
print(ans)