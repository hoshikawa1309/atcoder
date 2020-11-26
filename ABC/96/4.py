def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(n ** (1 / 2)) + 1):
        if n % k == 0:
            return False

    return True


N = int(input())
cnt = 0
for i in range(6, 55556, 5):
    if is_prime(i):
        print(i, end=' ')
        cnt += 1
        if cnt == N:
            print()
            exit()
