def cmb(n, r, mod=10**9+7):
    if ( r < 0 or r > n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10 ** 9 + 7 #出力の制限
N = 10 ** 4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

N , K = map(int,input().split())
A = list(map(int,input().split()))
establish = 1
expect = 0
for i in range(2 ** K):
    cnt = 0
    establish = 1
    for j in range(K):
        if i >> j & 1:
            cnt += 1
            establish *= (A[j] / N)
        else:
            establish *= (1 - (A[j] / N))
    expect += (cnt * establish )
print(expect * N)
ans = expect
for i in range(K):
    ans *= cmb(N , A[i])
    ans %= mod
print(ans)