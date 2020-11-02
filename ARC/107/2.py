N, K = map(int, input().split())
def solve(N, K):
    ans = 0
    for x in range(2, 2 * N + 1):
        y = x - K
        print(x, y)
        if x - N >= K:
            start_x = max(x - N, 1)
        else:
            start_x = 1
        if y - N >= K:
            start_y = max(y - N, 1)
        else:
            start_y = 1
        end_x = x - start_x
        end_y = y - start_y
        x_cnt = end_x - start_x + 1
        y_cnt = end_y - start_y + 1
        print('x_cnt', x_cnt)
        print('y_cnt', y_cnt)
        ans += x_cnt * y_cnt
    return  ans


def solve2(N, K):
    ans = 0
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            for c in range(1, N + 1):
                for d in range(1, N + 1):
                    if a + b - c - d == K:
                        ans += 1
    return  ans
print(solve(N, K))
print(solve2(N, K))
'''
for i in range(-10, 11):
    for j in range(-10, 11):
        if solve(i, j)!= solve2(i, j):
            print(i, j)
            print(solve(i, j))
            print(solve2(i, j))
'''