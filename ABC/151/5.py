MOD = 10 ** 9 + 7
def cmb(n, r, mod= 10 ** 9 + 7):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


max_sum = 0
min_sum = 0
mod = 10**9+7 #出力の制限
N = 10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


N , K = map(int, input().split())
A = list(map(int,input().split()))
A.sort()
A_rev = sorted(A , reverse=True)
MOD = 10 ** 9 + 7
ans = 0
for i in range(N - K + 1):
    min_sum += A[i] * cmb(N - i - 1 , i + 1)

    max_sum += A_rev[i] * cmb(N - i - 1 , i + 1)
    print(i)
ans = (max_sum - min_sum) % MOD
print(ans)