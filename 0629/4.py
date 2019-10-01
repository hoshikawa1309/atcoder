from scipy.special import comb

mod = 1000000007
N , K = map(int,input().split())
ans = 0
for i in range(1,K + 1):
    #tmp_ans = perm(N - K + i ,i) / i
    ans = comb(N - K + 1 , i) * comb(K - 1 , i - 1)
    print(int(ans % mod ))