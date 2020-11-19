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


divs = make_divisors(N)
sum_val = sum(divs)
sum_val -= N
if sum_val == N:
    print('Perfect')
elif sum_val < N:
    print('Deficient')
else:
    print('Abundant')