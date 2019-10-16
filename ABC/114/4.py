'''
import math
N = int(input())
factorial_N = math.factorial(N)
print(factorial_N)
def makedivisor(n):
    divisor = []
    for i in range(1 , int(n ** 0.5) + 1):
        if n % i ==0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)
    return divisor

ans = 0
div_list = makedivisor(factorial_N)
print(len(div_list))
print(sorted(div_list))
for i in div_list:
    tmp_list = makedivisor(i)
    #print(tmp_list)
    if len(tmp_list) == 75:
        ans += 1
print(ans)
'''
from collections import Counter
N = int(input())
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
lst = []
for i in range(1 , N + 1):
    lst.extend(prime_factorize(i))
print(lst)
print(Counter(lst))