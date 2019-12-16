import bisect
N , M = map(int,input().split())
X , Y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
now = 0
ans = 0
for i in range(N):
    if now > A[-1]:
        break
    idx = bisect.bisect_left(A , now)
    now = A[idx]
    now += X
    if now > B[-1]:
        break
    idx = bisect.bisect_left(B, now)
    now = B[idx]
    now += Y
    ans += 1
print(ans)