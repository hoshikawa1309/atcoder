from collections import Counter
N = int(input())
# N = 10000
T = list(int(input()) for _ in range(N))
T.sort()
sum_list = [T[0]]
for i in range(1, N):
    sum_list.append(sum_list[-1] + T[i])
# print(sum_list)
print(sum(sum_list))
T = Counter(T)
# T = Counter([1] * N)
ans = 1
MOD = 10 ** 9 + 7
memo = [1] * (10 ** 4)
for i in range(1, 10 ** 4):
    memo[i] = (memo[i - 1] * (i + 1)) % MOD

for val in T.values():
    ans *= memo[val - 1]
    ans %= MOD
print(ans)