from functools import lru_cache
N = input()
K = int(input())

## lru_cacheを使ってメモ化
@lru_cache(maxsize=None)
def rec(k,tight,sum_val):
    # 最後まで探索した時、問題条件に応じて1 or 0を返す
    if k == len(N):
        if sum_val == K and sum_val != 0:
            return 1
        else:
            return 0

    # 現在の桁がtightであるか否かで終了する条件を変更する
    x = int(N[k])
    if tight:
        r = x
    else:
        r = 9
    res = 0
    for i in range(r + 1):
        if i == 0:
            res += rec(k + 1 ,tight and i == r, sum_val)
        else:
            res += rec(k + 1, tight and i == r, sum_val + 1)

    return res



print(rec(0 , True , 0))