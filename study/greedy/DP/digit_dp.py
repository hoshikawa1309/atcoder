D = int(input())
N = input()
#dp = [10000][2][100]
mod = 10 ** 9 + 1

def rec(k,tight,sum_val):
    if k == len(N):
        if sum_val % D == 0 and sum_val != 0:
            return 1
        else:
            return 0
    x = int(N[k])
    if tight == 1:
        r = x
    else:
        r = 10
    res = 0
    for i in range(r):
        res += rec(k + 1 ,tight and i == r, sum_val + i )
        res %= mod

    return res



print(rec(0 , True , 0))