N = int(input())
# N = 2 * 10 ** 5
A = tuple(map(int, input().split()))
# A = [10 ** 9] * N
MOD = 10 ** 9 + 7
rev_sum_list = [0] * N
rev_sum_list[-1] = A[-1]
for i in range(N - 2, -1, -1):
    rev_sum_list[i] = (rev_sum_list[i + 1] + A[i]) % MOD
# print(rev_sum_list)
ans = 0
for i in range(1, N):
    ans += A[i - 1] * rev_sum_list[i]
    ans %= MOD
print(ans)