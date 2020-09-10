N, M = map(int, input().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

ans = 1
for i in make_divisors(M):
    work1 = i * N
    work2 = M - work1
    if work2 >= 0 and work2 % i == 0:
        ans = max(i, ans)
# print(make_divisors(M))
print(ans)