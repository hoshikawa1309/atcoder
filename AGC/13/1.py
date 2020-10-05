N = int(input())
A = list(map(int, input().split()))
if N < 3:
    print(1)
    exit()
ans = 1
work = [A[0]]
now = A[0]
for i in range(1, N):
    if now == A[i]:
        continue
    work.append(A[i])
    now = A[i]
A = work
for i in range(len(A) - 2):
    if A[i] < A[i + 1] > A[i + 2] or A[i] > A[i + 1] < A[i + 2]:
        ans += 1
print(ans)