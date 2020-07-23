N, K = map(int, input().split())
ans = 0
for x in range(1, N + 1):
    cnt = 0
    while x < K:
        cnt += 1
        x *= 2
    ans += (1 / N) * (1 / 2) ** cnt
print(ans)
