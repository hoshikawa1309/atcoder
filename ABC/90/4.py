N , K = map(int,input().split())
ans = 0
for i in range(K + 1, N + 1):
    before_range = max((N % i - K + 1) , 0)
    before_cnt = (N // i + 1)
    before = before_cnt * before_range
    after_range = min((i - 1) - (N % i) , (i - 1) - K + 1)
    after_cnt = (N // i)
    after = after_cnt * after_range
    now = before + after
    if K == 0:
        now -= 1
    #print(now)
    ans += now
print(ans)