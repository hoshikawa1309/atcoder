N, M = map(int, input().split())
if 2 * N >= M:
    print(M // 2)
else:
    c_cnt = M + N * 2
    print(c_cnt // 4)