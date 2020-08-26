N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
sum_A = sum(A)
A.sort(reverse=True)
for a in A:
    if a >= sum_A / (4 * M):
        cnt += 1
    else:
        break
if cnt >= M:
    print('Yes')
else:
    print('No')