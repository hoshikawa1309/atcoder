from functools import lru_cache
mod = 10 ** 9 + 7

## lru_cacheを使ってメモ化
@lru_cache(maxsize=None)
def rec(k,tight,not_zero):
    # 最後まで探索した時、問題条件に応じて1 or 0を返す
    if not_zero == K:
        return 1
    if k == len(N):
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
            res += rec(k + 1 ,tight and i == r, not_zero + 0)
        else:
            res += rec(k + 1, tight and i == r, not_zero + 1)
        res %= mod

    return res

N = input()
K = int(input())

print(rec(0 , True , 0))

