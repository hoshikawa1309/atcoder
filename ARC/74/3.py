H, W = map(int, input().split())
ans = float('inf')
if H % 3 == 0:
    ans = 0
else:
    ans = min(ans, W)

if W % 3 == 0:
    ans = 0
else:
    ans = min(ans, H)

for i in range(1, H):
    chocolate = []
    chocolate.append(i * W)
    chocolate.append((H - i) * (W // 2))
    if W % 2 == 1:
        chocolate.append((H - i) * (W // 2 + 1))
    chocolate.sort()
    ans = min(chocolate[-1] - chocolate[0], ans)

for i in range(1, W):
    chocolate = []
    chocolate.append(i * H)
    if H % 2 == 1:
        chocolate.append((W - i) * (H // 2 + 1))
    chocolate.append((W - i) * (H // 2))
    chocolate.sort()
    ans = min(chocolate[-1] - chocolate[0], ans)
print(ans)