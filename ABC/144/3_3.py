def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

10
N = int(input())
divisors = make_divisors(N)
ans = float('inf')
div_len = len(divisors)
if div_len % 2 == 0:
    i = div_len // 2
    j = div_len // 2 - 1
    ans = divisors[i] + divisors[j] - 2
else:
    ans = divisors[div_len // 2] * 2 - 2
print(ans)