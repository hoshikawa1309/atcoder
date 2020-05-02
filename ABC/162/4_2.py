N = int(input())
S = input()
r = g = b = 0
for s in S:
    if s == 'R':
        r += 1
    if s == 'G':
        g += 1
    if s == 'B':
        b += 1

ans = r * g * b
for i in range(N - 1):
    for j in range(i + 1, N):
        k = 2 * j - i
        if k >= N:
            continue
        if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            ans -= 1
print(ans)