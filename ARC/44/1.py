N = int(input())


def is_prime(n):
    if n == 1: return False

    for k in range(2, int(n ** (1 / 2)) + 1):
        if n % k == 0:
            return False

    return True


if is_prime(N) or (N != 1 and N % 2 != 0 and N % 3 != 0 and N % 5 != 0):
    print('Prime')
else:
    print('Not Prime')