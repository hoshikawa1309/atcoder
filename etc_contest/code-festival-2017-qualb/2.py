import bisect
N = int(input())
D = list(map(int, input().split()))
D.sort()
M = int(input())
T = list(map(int, input().split()))
for i in range(M):
    t = T[i]
    idx = min(bisect.bisect_left(D, t), len(D) - 1)
    d = D[idx]
    if t == d:
        D.pop(idx)
    else:
        print('NO')
        exit()
print('YES')

