import sys
sys.setrecursionlimit(10 ** 6)
N, M, Q = map(int, input().split())
Q = [list(map(int,input().split())) for _ in range(Q)]
ans = 0
A = []


def dfs():
    global A
    if len(A) == N:
        return
    global ans
    if len(A) == 0:
        start = 1
    else:
        start = A[-1]
    for i in range(start, M + 1):
        A.append(i)
        dfs()
        if len(A) != N:
            A.pop()
            continue
        # print(A)
        tmp_ans = 0
        for a, b, c, d in Q:
            if A[b - 1] - A[a - 1] == c:
                tmp_ans += d
        ans = max(ans, tmp_ans)
        A.pop()


dfs()
print(ans)