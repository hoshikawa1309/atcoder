N = int(input())
cooking = []

aoki = 0
for _ in range(N):
    a, b = map(int, input().split())
    cooking.append([a + b, a, b])
chokudai = 0
cooking.sort(reverse=True)
for i in range(0, N):
    if i % 2 == 0:
        chokudai += cooking[i][1]
    else:
        aoki += cooking[i][2]
ans = chokudai - aoki

print(ans)