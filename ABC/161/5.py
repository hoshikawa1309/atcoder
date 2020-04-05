N, K, C = map(int, input().split())
S = input()
is_one = False
now = 0
range_cnt = 0
ans = []
while now < N:
    if S[now] == 'o':
        maru_cnt = 1
        range_cnt += 1
        for i in range(C):
            now += 1
            if now >= N:
                break
            if S[now] == 'o':
                maru_cnt += 1
        now += 1
        if maru_cnt == 1:
            ans.append(now - C)
    else:
        now += 1
if K == range_cnt:
    print(*ans, sep='\n')
