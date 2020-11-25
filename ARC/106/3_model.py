import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, M = map(int, readline().split())
    if M < 0:
        print(-1)
    elif M == 0:
        i = 0
        for _ in range(N):
            i += 1
            L = i
            i += 1
            R = i
            print(L, R)
    else:
        if N - M >= 2:
            i = 0
            for _ in range(N - M - 2):
                i += 1
                L = i
                i += 1
                R = i
                print(L, R)
            i += 1
            print(i, 10 ** 9)
            for _ in range(M + 1):
                i += 1
                L = i
                i += 1
                R = i
                print(L, R)
        else:
            print(-1)


if __name__ == '__main__':
    main()
