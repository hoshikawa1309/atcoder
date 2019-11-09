'''
def main():
    from functools import lru_cache
    import sys
    sys.setrecursionlimit(10**6)
    def input():
        return sys.stdin.readline()[:-1]
    W = int(input())
    N , K = map(int,input().split())
    pictures = [list(map(int,input().split())) for _ in range(N)]

    @lru_cache(maxsize=None)
    def solve(i,w,k):
        if i == N:
            ret_val = 0
        elif w < pictures[i][0] or k + 1 > K:
            ret_val = solve(i+1 , w,k)
        else:
            ret_val = max(solve(i+1,w,k) , solve(i+1,w - pictures[i][0],k+1) + pictures[i][1])
        return ret_val

    print(solve(0,W,0))

main()

10
3 2
4 20
3 40
6 100

'''
W = int(input())
N, K = map(int, input().split())
pictures = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(K + 1)] for _ in range(W + 1)] for _ in range(N + 1)]
for i in range(N-1,-1,-1):
    for j in range(W+1):
        for k in range(K):
            if j < pictures[i][0] or k == K:
                dp[i][j][k] = dp[i+1][j][k]
            else:
                dp[i][j][k] = max(dp[i+1][j][k] , dp[i+1][j - pictures[i][0]][k + 1] + pictures[i][1])
print(dp[0][W][0])
