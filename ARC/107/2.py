def f(x):
    return min(x - 1, 2 * N - x + 1)

N, K = map(int, input().split())
ans = 0
for ab in range(2, 2 * N + 1):
    cd = ab - K
    if cd < 2 or 2 * N + 1 < cd:
        continue
    ans += f(ab) * f(cd)
print(ans)