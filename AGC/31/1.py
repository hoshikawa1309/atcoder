from collections import Counter
N = int(input())
S = input()
S_c = Counter(S)
ans = 1
mod = 10 ** 9 + 7
for val in S_c.values():
    ans *= (val + 1)
    ans %= mod

print(ans - 1)