import bisect
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
A_cumulative_sum = [0]
B_cumulative_sum = [B[0]]
for i in range(N):
    A_cumulative_sum.append(A[i] + A_cumulative_sum[i])
for i in range(1, M):
    B_cumulative_sum.append(B[i] + B_cumulative_sum[i - 1])

for i in range(N + 1):

    if K < A_cumulative_sum[i]:
        remaining_time = K
        idx = bisect.bisect_right(B_cumulative_sum, remaining_time)
        ans = max(ans, idx)
        break
    else:
        remaining_time = K - A_cumulative_sum[i]
        idx = bisect.bisect_right(B_cumulative_sum, remaining_time)
        ans = max(ans, i + idx)
print(ans)

# 113897