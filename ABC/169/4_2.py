def prime_factorize(n):
    '''
    素因数分解のリストを返す。n == 1のとき[]になるので注意。
    :param n:int
    素因数分解する自然数
    :return: list
    素因数分解した結果。

    例
    n : 10
    primes : [[2, 1], [5, 1]]
    '''
    primes = []
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i != 0:
            continue
        num = 0
        while n % i == 0:
            num += 1
            n //= i
        primes.append([i, num])
    if n != 1:
        primes.append([n, 1])
    return primes

N = int(input())
pf = prime_factorize(N)
res = 0
for p, e in pf:
    tmp = 0
    cur = 1
    while e >= cur:
        e -= cur
        cur += 1
        tmp += 1
    res += tmp
print(res)