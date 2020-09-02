N = int(input())
A = [int(input()) for i in range(N)]
A.sort()
work = []
ans = 0
if N % 2 == 1:
    before = A[:N // 2]
    after = A[N // 2 + 1:]
    median = A[N // 2]
    for i in range(N // 2):
        work.append(after[i])
        work.append(before[i])
    work.append(median)
    tmp1 = 0
    tmp2 = 0
    for i in range(N - 1):
        tmp1 += abs(work[i] - work[i + 1])
    t = work.pop()
    work.insert(0, t)
    for i in range(N - 1):
        tmp2 += abs(work[i] - work[i + 1])
    ans = max(tmp1, tmp2)

else:
    before = A[:N // 2]
    after = A[N // 2:]
    for i in range(N // 2):
        work.append(after[i])
        work.append(before[i])
    for i in range(N - 1):
        ans += abs(work[i] - work[i + 1])
print(ans)


