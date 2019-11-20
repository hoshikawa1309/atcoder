'''
import math
x , y = map(int,input().split())
flag = False
MOD = 10 ** 9 + 7
for s in range(max(x,y)):
    if 2 * x - 3 * s == y:
        flag = True
        break
t = x - 2 * s
if flag:
    #print(math.factorial(t+s)//(math.factorial(t) * math.factorial(s)) % MOD)
    sum_val = 1
    for i in range(t + s , max(t , s) - 1,-1):
        sum_val *= i
        sum_val %= MOD
else:
    print(0)

'''
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
#出力の制限
#フェルマーの小定理なので、素数のみ使用
mod = 10**9+7 #出力の制限
N = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
flag = False
x , y = map(int,input().split())
MOD = 10 ** 9 + 7
for s in range(max(x,y)):
    if 2 * x - 3 * s == y:
        flag = True
        break
t = x - 2 * s
if flag:
    print(cmb((t+s),s,mod))
else:
    print(0)
