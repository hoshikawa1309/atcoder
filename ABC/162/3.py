# from math import gcd


def gcd(a, b):
    if a < b:
        a, b = b , a
    while b != 0:
        a, b = b, a % b
    return a
K = int(input())
ans = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        tmp_ans = gcd(a, b)
        for c in range(1, K + 1):
            ans += gcd(tmp_ans, c)
print(ans)
