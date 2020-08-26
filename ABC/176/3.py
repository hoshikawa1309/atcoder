N = int(input())
A = list(map(int, input().split()))
ans = 0
now = A[0]
for a in A:
    if now >= a:
        ans += now - a
    else:
        now = a
print(ans)