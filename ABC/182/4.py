N = int(input())
A = list(map(int, input().split()))
s = [0] * N
now = 0
s[0] = A[0]
for i in range(1, N):
    s[i] = s[i - 1] + A[i]

max_val = 0
ans = 0
for v in s:
    max_val = max(v, max_val)
    ans = max(now + max_val, ans)
    now += v
print(ans)