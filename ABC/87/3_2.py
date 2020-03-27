N = int(input())
A = list(list(map(int, input().split())) for _ in range(2))
ans = 0
for i in range(N):
    now = 0
    now += sum(A[0][0: i + 1])
    now += sum(A[1][i: N])
    if ans < now:
        ans = now
print(ans)