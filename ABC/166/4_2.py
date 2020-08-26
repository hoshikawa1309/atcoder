from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
ans = 0
d = defaultdict(int)
for now, high in enumerate(A):
    i = now + high
    j = now - high
    if d[j] > 0:
        ans += d[j]
    if i < N:
        d[i] += 1
print(ans)
