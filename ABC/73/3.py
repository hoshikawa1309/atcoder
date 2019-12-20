from collections import Counter
N = int(input())
A = Counter([int(input()) for _ in range(N)])
ans = 0
for val in A.values():
    if val % 2 == 1:
        ans += 1
print(ans)