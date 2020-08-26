
def solve(n, m, s, t):
    import math
    def lcm(x, y):
        return (x * y) // math.gcd(x, y)
    L = lcm(n, m)

    X = [''] * L
    for i in range(n):
        X[i * (L // n)] = s[i]
    for i in range(m):
        now = X[i * (L // m)]
        if now == '':
            X[i * (L // m)] = t[i]
        elif now == t[i]:
            continue
        else:
            print(-1)
            exit()
    # print(X)
    print(L)

if __name__ == '__main__':

    N, M = map(int, input().split())
    S = input()
    T = input()
    solve(N, M, S, T)
    '''
    import random
    for N in range(1, 10):
        for M in range(1, 10):
            S = ''
            T = ''
            for _ in range(N):
                S += chr(random.randint(97, 122))
            for _ in range(M):
                T += chr(random.randint(97, 122))
            print(S)
            print(T)
            solve(N, M, S, T)
    '''