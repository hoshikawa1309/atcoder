K, N = map(int, input().split())
A = list(map(int, input().split()))
max_len = (K - A[-1]) + A[0]
now = A[0]
for i in range(1, N):
    now_len = A[i] - now
    if max_len < now_len:
        max_len = now_len
    now = A[i]
print(K - max_len)