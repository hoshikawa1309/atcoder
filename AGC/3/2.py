N = int(input())
A = list(int(input()) for _ in range(N))
ans = A[0] // 2
remainder = A[0] % 2
for idx, a in enumerate(A):
    if idx == 0:
        continue
    ans += a // 2
    if remainder == 1 and a % 2 == 1:
        ans += 1
        remainder = 0
    elif remainder == 0 and a % 2 == 1:
        remainder = 1
    else:
        remainder = 0
print(ans)


