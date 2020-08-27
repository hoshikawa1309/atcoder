from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
for i, a in enumerate(A):
    d[i + a] += 1
ans = 0
for j, a in enumerate(A):
    ans += d[j - a]
print(ans)