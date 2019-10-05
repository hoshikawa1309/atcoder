from pprint import pprint
'''
## O(1)のパターン
N , Z , W = map(int , input().split())

a = list(map(int , input().split()))

print(max(abs(a[N - 2] - a[N - 1]), abs(a[N - 1] - W)))
'''
## DPを使って解くとき
N , Z , W = map(int , input().split())
a = list(map(int , input().split()))
a.reverse()
a += [W]
#print(a)
memo = [[-1]* (N + 1) , [-1] * (N + 1)]
def DP(n , turn):

    if n == 1:
        #print(memo[turn][n])
        return abs(a[0] - W)
    if memo[turn][n] != -1:
        return memo[turn][n]
    if turn == 1:
        #print("turn : 1")
        tmp_max = 0
        for i in range(1 , n + 1):
            if i == n:
                tmp_max = max(tmp_max , abs(a[0]-W))
            else:
                tmp_max = max(tmp_max , DP(n - 1,1 - turn))
        #print("tmp_max : ",tmp_max)
        memo[turn][n] = tmp_max
        return tmp_max
    if turn == 0:
        tmp_min = 10 ** 9
        #print("turn : 0")
        for i in range(1 , n + 1):
            if i == n:
                tmp_min = min(tmp_min , abs(a[0]-W))
            else:
                tmp_min = min(tmp_min , DP(n - 1,1 - turn))
        #print("tmp_min : ",tmp_min)
        memo[turn][n] = tmp_min
        return tmp_min



print(DP(N , 1))
#print(memo)
