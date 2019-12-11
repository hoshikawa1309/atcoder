import collections
def prime_factorize(n):
    a = []
    if n == 1:
        a.append(1)
        return a
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
N = int(input())
prime_lst = [0] * N
for i in range(1 , N + 1):
    c = collections.Counter(prime_factorize(i))
    for key , val in c.items():
        prime_lst[key - 1] += int(val)
ans = 1
#print(prime_lst)
prime_lst.pop(0)
for l in prime_lst:
    if l == 0:
        continue
    ans *= (l + 1)
    ans %= 10 ** 9 + 7
print(ans)



