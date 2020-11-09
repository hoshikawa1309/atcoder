N = int(input())
A = list(map(int, input().split()))
cnt = [0] * 1001

for a in A:
    for x in range(2, a + 1):
        if a % x == 0:
            cnt[x] += 1
ans = 0
max_val = -1
for idx, val in enumerate(cnt):
    if val >= max_val:
        ans = idx
        max_val = val
# print(cnt)
print(ans)