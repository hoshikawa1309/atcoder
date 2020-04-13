N = int(input())
A = list(int(input()) for _ in range(N))
Flags = [False] * (10 ** 5)
ans = 0
for a in A:
    if Flags[a - 1]:
        ans += 1
    else:
        Flags[a - 1] = True
print(ans)