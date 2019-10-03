import math
N = int(input())
A = list(map(int , input().split()))
#result = 0;
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

def sigma2(func, frm, to):
    result1 = 0; #答えの受け皿
    for i in range(frm, to+1):
        result1 += func(A[frm - 1],A[i])
        #ここで関数を呼び出す。ちなみにここではi = x
    return result1
def sigma(sigma2, frm, to):
    result = 0; #答えの受け皿
    for i in range(frm, to+1):
        result += sigma2(lcm,i + 1,N - 1)
        result %= 998244353
        #ここで関数を呼び出す。ちなみにここではi = x
    return result

if __name__ == "__main__":
    print(sigma(sigma2,0,N - 2) )