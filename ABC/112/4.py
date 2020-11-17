def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


N, M = map(int,input().split())
divisors_list = make_divisors(M)
# print(divisors_list)
ans = 0
for div in divisors_list:
    if (M // div) // N > 0:
        ans = max(ans, div)
print(ans)