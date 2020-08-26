N = int(input())
prime_cnt = [0] * 1000
ans = 0
for i in range(2, N + 1):
    work = i
    for j in range(2, int(i ** (1 / 2)) + 1):
        while work % j == 0:
            prime_cnt[j - 1] += 1
            work //= j
    if work != 1:
        prime_cnt[work - 1] += 1
# print(prime_cnt)
ans = 1
mod = 10 ** 9 + 7
for cnt in prime_cnt:
    if cnt:
        ans *= (cnt + 1)
        ans %= mod
print(ans)