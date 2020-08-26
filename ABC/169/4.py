def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


N = int(input())
div_list = make_divisors(N)
print(div_list)
ans = 0
print(N)
used = set()
while N != 1:
    for div in div_list:
        if div == 1 or N % div != 0 or div in used:
            continue
        if N == 1:
            break
        ans += 1
        N //= div
        used.add(div)
        print(div, N)
    else:
        break
print(ans)