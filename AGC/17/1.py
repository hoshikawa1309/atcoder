import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N , P = map(int,input().split())
A = list(map(int,input().split()))
odd_num = 0
even_num = 0
for a in A:
    if a % 2 == 1:
        odd_num += 1
    else:
        even_num += 1
ans = 0

if P == 1:
    if odd_num == 0:
        ans = 0
    else:
        for i in range(1, N + 1, 2):
            ans += combinations_count(N, i)
else:
    if odd_num == 0:
        ans = 2 ** even_num
    else:
        for i in range(0, N + 1, 2):
            ans += combinations_count(N, i)
print(ans)
