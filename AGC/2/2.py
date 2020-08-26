def solve():
    N, M = map(int, input().split())
    contains_redball = [False] * N
    contains_redball[0] = True
    balls_cnt = [1] * N
    for _ in range(M):
        x, y = map(int, input().split())
        x, y = x - 1, y - 1
        balls_cnt[x] -= 1
        balls_cnt[y] += 1
        if contains_redball[x]:
            contains_redball[y] = True
        if balls_cnt[x] == 0:
            contains_redball[x] = False
    print(sum(contains_redball))

if __name__ == '__main__':
    solve()