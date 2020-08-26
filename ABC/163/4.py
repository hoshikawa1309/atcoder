N, K = map(int, input().split())
min_val = 0
max_val = 0
for i in range(K):
    max_val += N - i
    min_val += i
# print(min_val)
# print(max_val)

ans = 0
mod = 10 ** 9 + 7
for i in range(K, N + 2):
    ans += max_val - min_val + 1
    ans %= mod
    min_val += i
    max_val += N - i
print(ans)