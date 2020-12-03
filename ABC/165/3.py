import sys
sys.setrecursionlimit(10 ** 6)
N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(Q)]
ans = 0
def dfs(A):
    if len(A) == N:
        global ans
        sum_val = 0
        for a, b, c, d in abcd:
            a, b = a - 1, b - 1
            if A[b] - A[a] == c:
                sum_val += d
        ans = max(ans, sum_val)
    else:
        for i in range(A[-1], M + 1):
            A.append(i)
            dfs(A)
            A.pop()


dfs([1])
print(ans)