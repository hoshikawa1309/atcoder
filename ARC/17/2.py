N, K = map(int, input().split())
A = tuple(int(input()) for _ in range(N))
ans = 0
high = []
num = 0
for i in range(N - 1):
    if A[i] < A[i + 1]:
        num += 1
    else:
        high.append(num + 1)
        num = 0
else:
    if num:
        high.append(num + 1)

for h in high:
    ans += max(0, h - K + 1)
print(ans)