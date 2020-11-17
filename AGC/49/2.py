N = int(input())
s = list(map(lambda x: int(x), input()))
t = list(map(lambda x: int(x), input()))
ans = 0
for i in range(N - 1, 0, -1):
    if s[i] == t[i]:
        continue
    s[i] = 1 - s[i]
    s[i - 1] = 1 - s[i - 1]
    ans += 1

for i in range(N):
    if s[i] == t[i]:
        continue
    print(-1)
    exit()