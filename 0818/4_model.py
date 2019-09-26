import sys

sys.setrecursionlimit(5 * 10**5)
input=sys.stdin.readline

N, Q = list(map(int, input().split()))

M = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    M[a-1].append(b-1)
    M[b-1].append(a-1)

ans = [0] * N
for _ in range(Q):
    p, x = list(map(int, input().split()))
    ans[p-1] += x

Q = [0]

while Q:
    current = Q.pop()

    for i in M[current]:
        ans[i] += ans[current]
        M[i].remove(current)

    Q += M[current]

print(' '.join(map(str, ans)))
