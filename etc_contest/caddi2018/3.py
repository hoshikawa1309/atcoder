import bisect
N, P = map(int, input().split())
if N == 1:
    print(P)
    exit()

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


div_list = make_divisors(P)
ans = 1
for i in range(2, 10 ** 6 + 1):
    idx = bisect.bisect_left(div_list, i ** N)
    if i ** N > div_list[-1]:
        break
    if i ** N == div_list[min(idx, len(div_list) - 1)]:
        ans = i
print(ans)