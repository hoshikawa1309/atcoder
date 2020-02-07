N = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
b = [0] * N
M = 0
for i in range(N, 0, -1):
    ball = 0
    for j in range(i + i, N + 1, i):
        ball ^= b[j - 1]
    b[i - 1] = ball ^ a[i]
M = sum(b)
print(M)
for i in range(N):
    if b[i]:
        print(i + 1, end = ' ')
