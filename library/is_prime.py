def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(n ** (1 / 2)) + 1):
        if n % k == 0:
            return False

    return True

if __name__ == '__main__':
    for i in range(1, 21):
        print(i, is_prime(i))