N = int(input())
P = list(map(int, input().split()))
now = P[0]
ans = 1
for i in range(1, N):
    if now >= P[i]:
        now = P[i]
        ans += 1
print(ans)