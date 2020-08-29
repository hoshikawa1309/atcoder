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

if __name__ == '__main__':
    import time
    # 最大値を用いてインスタンス化
    object = prime_factorize_by_osa_k(1000000)
    print(object.osa_k(50))



