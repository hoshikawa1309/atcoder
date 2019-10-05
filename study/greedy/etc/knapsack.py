from pprint import pprint
N , W = map(int, input().split())
value = []
weight = []
for _ in range(N):
    v , w = map(int , input().split())
    value.append(v)
    weight.append(w)

def solve( i , capacity):
    if i == N:
        return 0
    elif capacity < weight[i]:
        return solve(i + 1,capacity)
    else:
        return max(solve(i + 1,capacity) , solve(i + 1 , capacity - weight[i]) + value[i])

def memo_solve(i , W):
    memo = [[-1 for _ in range(W + 1)] for _ in range(N + 1)]

    def solve(i, capacity):
        if memo[i][capacity] >= 0:
            return memo[i][capacity]
        if i == N:
            res_value = 0
        elif capacity < weight[i]:
            res_value = solve(i + 1, capacity)
        else:
            #memo[i][capacity] = max(solve(i + 1, capacity), solve(i + 1, capacity - weight[i]) + value[i])
            res_value = max(solve(i + 1, capacity), solve(i + 1, capacity - weight[i]) + value[i])
        memo[i][capacity] = res_value
        #pprint(memo)
        return res_value
    #pprint(memo)
    return solve(i,W)

if __name__ == "__main__":
    print(memo_solve(0 , W))
    #print(solve(0,W))