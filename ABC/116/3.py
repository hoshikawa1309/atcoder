N = int(input())
flowers = list(map(int, input().split()))
now = 0
ans = 0
for h in flowers:
    if now < h:
        ans += (h - now)
        now = h
    else:
        now = h
print(ans)