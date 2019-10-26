import sys
sys.setrecursionlimit(10 ** 6)
n , m = map(int,input().split())
coins = list(map(int,input().split()))
coins.sort(reverse=True)
dp = [[float("inf")]*(n + 1) for _ in range(m + 1)]
def solve(i , value):
    if dp[i][value] != float("inf"):
        return dp[i][value]
    if i == m - 1 or value == 0:
        ret_val = value
    elif coins[i] > value:
        ret_val = solve(i + 1,value)
    else:
        ret_val = min(solve(i + 1,value) , solve(i,value - coins[i]) + 1)
    dp[i][value] = ret_val
    return ret_val

solve(0 , n)
print(dp[0][n])
#pprint.pprint(dp)

'''
620 6
1 5 10 50 100 500

50000 20
1 92 1377 3168 7095 1170 1809 5046 3225 1054 4016 142 108 6430 3970 48 8416 4909 114 6968
'''