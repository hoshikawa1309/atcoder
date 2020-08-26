N, D = map(int, input().split())
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    dis = (x ** 2 + y ** 2) ** (1 / 2)
    if dis <= D:
        ans += 1
print(ans)