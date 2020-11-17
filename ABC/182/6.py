N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
A.sort(reverse=True)
for y in range(X, X + 1000000):
    change = y - X
    s1 = set()
    s2 = set()
    for a in A:
        if y >= a:
            y -= (y // a) * a
            s1.add(a)
        if change >= a:
            change -= (change // a) * a
            s2.add(a)
    if len(s1 & s2) == 0:
        ans += 1
print(ans)
