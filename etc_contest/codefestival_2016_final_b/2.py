N = int(input())
cnt = [False] * 10001
now = 0
idx = 0
for i in range(1, 10001):
    if now >= N:
        break
    now += i
    cnt[i] = True

if now != N:
    for i in range(10000, 0, -1):
        if now == N:
            break
        elif cnt[i] and now - i >= N:
            cnt[i] = False
            now -= i

for i in range(10001):
    if cnt[i]:
        print(i)