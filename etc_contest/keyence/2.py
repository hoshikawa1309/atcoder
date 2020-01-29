N = int(input())
robots = []
for _ in range(N):
    X, L = map(int, input().split())
    robots.append([X + L, X - L])
robots.sort()
now = -float("inf")
ans = 0
for i in range(N):
    if robots[i][1] >= now:
        now = robots[i][0]
        ans += 1
print(ans)
