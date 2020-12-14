import math
N, M = map(int,input().split())
if M == 0:
    print(1)
    exit()
A = list(map(int,input().split()))
A.sort()
now = 0
diff = []
for Ai in A:
    if Ai - now - 1 == 0:
        now = Ai
        continue
    diff.append(Ai - now - 1)
    now = Ai
if now != N:
    diff.append(N - now)
# print(diff)
if not diff:
    print(0)
    exit()
k = min(diff)
ans = 0
for d in diff:
    ans += math.ceil(d / k)
print(ans)