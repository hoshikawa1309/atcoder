from collections import Counter
N = int(input())
A = list(map(int, input().split()))
s = [0] * N
s[0] = A[0]
for i in range(1, N):
    s[i] = s[i - 1] + A[i]
s_c = Counter(s)
ans = s_c[0]
for key, val in s_c.items():
    ans += val * (val - 1) // 2
print(ans)