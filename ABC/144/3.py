N = int(input())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
#lst = prime_factorize(N)
lst = make_divisors(N)
lst.sort()
#print(lst)
if len(lst) == 2:
    print(lst[-1] - 1)
else:
    if len(lst) % 2 == 0:
        print(lst[len(lst)//2] + lst[len(lst) // 2 - 1] - 2)
    else:
        print(lst[len(lst) // 2] * 2 - 2)