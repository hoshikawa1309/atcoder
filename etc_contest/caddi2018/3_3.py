def solve(N, P):
    prime_list = []
    for i in range(2, int(P ** (1 / 2)) + 1):
        cnt = 0
        while P % i == 0:
            cnt += 1
            P //= i
        if cnt:
            prime_list.append([i, cnt])
    if P != 1:
        prime_list.append([P, 1])

    ans = 1
    for prime, cnt in prime_list:
        if cnt >= N:
            ans *= prime ** (cnt // N)
    return ans
    # print(ans)

def solve2(N, P):
    import bisect
    if N == 1:
        return P
        # exit()

    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        divisors.sort()
        return divisors

    div_list = make_divisors(P)
    ans = 0
    for i in range(10 ** 6 + 1):
        idx = bisect.bisect_left(div_list, i ** N)
        if i ** N == div_list[min(idx, len(div_list) - 1)]:
            ans = i
    return ans

if __name__ == '__main__':
    n, p = map(int, input().split())
    print(solve(n, p))
    print(solve2(n, p))
    for n in range(1, 10000):
        for p in range(1,10000):
            if n % 1000 == 0:
                print(n)
            if solve(n, p) != solve2(n, p):
                print(n, p)
                print(solve(n, p))
                print(solve2(n, p))