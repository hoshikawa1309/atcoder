N, M = map(int, input().split())
shops = list(list(map(int, input().split())) for _ in range(N))
shops.sort()
ans = 0
for value, count in shops:
    tmp_M = max(M - count , 0)
    ans += (M - tmp_M) * value
    M = tmp_M
    if M == 0:
        break
print(ans)
