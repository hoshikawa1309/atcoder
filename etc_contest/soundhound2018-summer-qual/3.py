n, m, d = map(int, input().split())
cnt = 0
if d == 0:
    cnt = n
else:
    cnt = 2 * (n - d)
print(cnt / n ** 2 * (m - 1))