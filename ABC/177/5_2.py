class prime_factorize_by_osa_k():
    def __init__(self, max_val):
        '''
        割ることが出来る最小の値を格納したリストを返す
        :param max_val:
        :return:
        '''
        self.minFactor = [-1] * (max_val + 1)
        for i in range(2, max_val + 1):
            if self.minFactor[i] == -1:
                self.minFactor[i] = i
                # エラトステネスの篩と同様の処理を行う
                for j in range(i * i, max_val + 1, i):
                    if self.minFactor[j] == -1:
                        self.minFactor[j] = i

    def osa_k(self, n):
        '''
        preprocessをしたあと、O(logN)で素因数分解を行う。nの最大値をn_maxとする。
        :param n:
        :return:
        '''
        from collections import defaultdict
        d = defaultdict(int)
        now = n
        while now > 1:
            d[self.minFactor[now]] += 1
            now //= self.minFactor[now]
        return d
def gcd(a, b):
    while b: a, b = b, a % b
    return a

N = int(input())
A = list(map(int, input().split()))
# N = 10 ** 6
# A = [10 ** 6] * N
ob = prime_factorize_by_osa_k(10 ** 6)
pairwise = False
prime_key = set(ob.osa_k(A[-1]).keys())
break_flag = False
prime_flags = [False] * (10 ** 6 + 1)
for i in range(N):
    for key in ob.osa_k(A[i]).keys():
        if prime_flags[key]:
            break_flag = True
            break
        else:
            prime_flags[key] = True
    if break_flag:
        break
else:
    pairwise = True
print(sum(prime_flags))
if pairwise:
    print('pairwise coprime')
    exit()
work = gcd(A[0], A[1])
for i in range(2, N):
    work = gcd(work, A[i])
if work != 1:
    print('not coprime')
else:
    print('setwise coprime')