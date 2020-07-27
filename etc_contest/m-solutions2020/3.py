N, K = map(int, input().split())
A = list(map(int, input().split()))
for i in range(K, N):
    # next_sum_val = now_sum_val // A[i - K] * A[i]
    if A[i] > A[i - K]:
        print('Yes')
    else:
        print('No')
    # now_sum_val = next_sum_val