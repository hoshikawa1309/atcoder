R, G, B, N = map(int, input().split())

ans = 0
for r in range(N + 1):
    for g in range(N + 1):
        ball = N - r * R - g * G
        check = (ball / B)
        if check.is_integer() and check >= 0:
            ans += 1
print(ans)