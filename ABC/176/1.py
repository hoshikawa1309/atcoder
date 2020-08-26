N, X, T = map(int, input().split())
ans = (N // X) * T
if N % X:
    ans += T
print(ans)

