L, X, Y, S, D = map(int, input().split())
ans = 0
dis = abs(D - S)
if D > S:
    if X >= Y:
        ans = dis / (Y + X)
    else:
        ans = min(dis / (Y + X), (L - dis) / (Y - X))
else:
    if X >= Y:
        ans = (L - dis) / (Y + X)
    else:
        ans = min(dis / (Y - X), (L - dis) / (Y + X))
print(ans)