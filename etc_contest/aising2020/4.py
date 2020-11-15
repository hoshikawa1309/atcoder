def popcount(k):
    ret_val = bin(k).count('1')
    return ret_val


def f(n):
    ret_val = 1
    while n:
        n = n % popcount(n)
        ret_val += 1
    return ret_val


N = int(input())
X = input()
if N == 1:
    if X == '1':
        print(0)
    else:
        print(1)
    exit()
dp1 = [0] * N
dp1[0] = 1
dp2 = [0] * N
dp2[0] = 1
bit = X.count('1')
if bit == 0:
    for i in range(N):
        print(1)
elif bit == 1:
    for i in range(N):
        if X[i] == '1':
            print(0)
        else:
            work = (pow(2, N - X.index('1') - 1, 2) + pow(2, N - i - 1, 2)) % 2
            if work == 0:
                print(1)
            else:
                print(f(work))
else:
    for i in range(1, N):
        dp1[i] = (2 * dp1[i - 1]) % (bit + 1)
        dp2[i] = (2 * dp2[i - 1]) % (bit - 1)
    dp1_sum = 0
    dp2_sum = 0
    for i in range(N):
        if X[i] == '1':
            dp1_sum += dp1[N - i - 1]
            dp2_sum += dp2[N - i - 1]
    for i in range(N):
        if X[i] == '1':
            work = (dp2_sum - pow(2, N - i - 1, bit - 1)) % (bit - 1)
        else:
            work = (dp1_sum + pow(2, N - i - 1, bit + 1)) % (bit + 1)
        if work == 0:
            print(1)
        else:
            print(f(work))
