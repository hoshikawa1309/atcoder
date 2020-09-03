# N, K = map(int, input().split())
def solve(N):
    K = 10 ** 5
    # A = list(map(int, input().split()))
    A = [0] * N
    for j in range(K):
        if len(set(A)) == 1 and A[0] == N:
            print('N :{}, change_cnt : {}'.format(N, j))
            break
        work = [0] * (N + 1)
        for i in range(N):
            a = A[i]
            idx0 = max(0, i - a)
            idx1 = min(N, i + a + 1)
            work[idx0] += 1
            work[idx1] -= 1
        now = 0
        for i in range(N):
            now += work[i]
            A[i] = now
    # print(*A)

if __name__ == '__main__':
    for i in range(99990, 100000):
        solve(i)