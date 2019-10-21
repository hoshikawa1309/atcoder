N , W = map(int , input().split())
value = []
weight = []
dp = [[0] * (N + 1) for _ in range(N)]
for _ in range(N):
    v , w = map(int ,input().split())
    value.append(v)
    weight.append(w)

def knapsack(i , j):
    dp = [[-1] * (W + 1) for _ in range(N + 1)]
    def solve(i , j):
        if dp[i][j] != -1:
            return dp[i][j]
        if i == N:
            retval = 0
        elif j < weight[i]:
            retval = solve(i + 1 , j)
        else:
            retval = max(solve(i + 1 , j) , solve(i + 1 , j - weight[i]) + value[i])
        dp[i][j] = retval
        return retval
    ans = solve(0,W)
    return ans

if __name__ == "__main__":
    print(knapsack(0 , W))