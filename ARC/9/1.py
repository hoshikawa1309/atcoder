N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

cnt = 0
A = A[::-1]
B = B[::-1]
for a, b in zip(A, B):
    if (a + cnt) % b == 0:
        continue
    cnt += b - ((a + cnt) % b)
print(cnt)
