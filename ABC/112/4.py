'''
def gcd(x,y):
    while y != 0:
        x, y = y , x % y
    return x
N , M = map(int,input().split())
ans = float('inf')
min_val = 0
for i in range(N , M):
    min_val = gcd(i,i + 1)
    if min_val < ans:
        ans = min_val
print(ans)
'''

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
N , M = map(int,input().split())
divisors_list = make_divisors(M)
divisors_list.sort(reverse=True)
print(divisors_list)
for val in divisors_list:
    if val * N <= M:
        break
print(val)