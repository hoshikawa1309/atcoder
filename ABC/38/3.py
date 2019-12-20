N = int(input())
A = list(map(int,input().split()))
now = A[0]
cnt = 1
ans = 0
for i in range(1 , N):
    if now < A[i]:
        cnt += 1
        now = A[i]
    else:
        ans += cnt * (cnt + 1) // 2
        cnt = 1
    now = A[i]
ans += cnt * (cnt + 1) // 2
print(ans)