N, A, B = map(int , input().split())
X = list(map(int,input().split()))
now = X[0]
ans = 0
for i in range(1, len(X)):
    if (X[i] - now) * A > B:
        ans += B
    else:
        ans += (X[i] - now) * A
    now = X[i]
print(ans)