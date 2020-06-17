import math
def solve():
    def is_prime(n):
        if n == 1: return False
        for k in range(2, int(math.sqrt(n)) + 1):
            if n % k == 0:
                return False
        return True

    def gcd( x, y ):
        while y != 0:
            x, y = y, x%y
        return x

    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)
        divisors.sort()
        return divisors

    A , B = map(int , input().split())

    gcd_value = gcd(A , B)
    cd = []
    div = make_divisors(gcd_value)
    for value in div:
        if A % value == 0 and B % value == 0 and is_prime(value):
            cd.append(value)
    print(len(cd) + 1)

if __name__ == "__main__":
    solve()