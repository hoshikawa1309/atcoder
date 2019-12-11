N , x = map(int,input().split())
A = list(map(int,input().split()))
delta = max( 0 , A[0] - x)
ans = delta
A[0] -= delta
for i in range(1 , N):
    delta = max(0 , A[i] + A[i - 1] - x)
    ans += delta
    A[i] -= delta
print(ans)