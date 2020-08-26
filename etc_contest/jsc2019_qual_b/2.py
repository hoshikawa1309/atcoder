N, K = map(int, input().split())
# N, K = 3, 3
A = list(map(int, input().split()))
# A = [i for i in range(3, 0, -1)]
mod = 10 ** 9 + 7
ans = 0
x = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            x += 1
ans += x * K
ans %= mod

cnt = [0] * N
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            cnt[i] += 1

cnt_sum = sum(cnt)
x = ((K - 1) * K // 2) % mod

ans += cnt_sum * x
ans %= mod
print(ans)
# 845502410
# 185297239