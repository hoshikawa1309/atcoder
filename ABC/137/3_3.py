from collections import Counter
import math
def combination2(n):
    return math.factorial(n) // (math.factorial(n - 2) * math.factorial(2))

N = int(input())
l = []
for _ in range(N):
    tmp = input()
    tmp = sorted(tmp)
    l.append(''.join(tmp))

l = Counter(l)
ans = 0
for key, value in l.items():
    if value >= 2:
        ans += combination2(value)
print(ans)


