def solve1(x):
    ret_val = 0
    t = -1
    x.sort()
    for i in range(N):
        if t < x[i][0]:
            ret_val += 1
            t = x[i][1]
    return ret_val



def solve2(x):
    ret_val = 0
    t = -1
    x.sort(key=lambda a:a[1])
    for i in range(N):
        if t < x[i][0]:
            ret_val += 1
            t = x[i][1]
    return ret_val


N, M = map(int, input().split())
if N == 1 and M == 0:
    print(1, 2)
    exit()
if M < 0 or max(0, N - 2) < M:
    print(-1)
    exit()

ans = []
for i in range(1, 2 * N, 2):
    ans.append([i, i + 1])
if M != 0:
    ans[N - M - 2][1] = 10 ** 9
for row in ans:
    print(*row)
'''
print(solve2(ans))
print(solve1(ans))
print(solve2(ans) - solve1(ans))
'''