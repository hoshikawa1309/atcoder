N, T = map(int, input().split())
A = []
B = []
diff = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    diff.append(a - b)
diff.sort(reverse=True)
if sum(A) <= T:
    print(0)
    exit()
if sum(B) > T:
    print(-1)
    exit()
ans = 0
now = sum(A)
for d in diff:
    now -= d
    ans += 1
    if now <= T:
        break
print(ans)