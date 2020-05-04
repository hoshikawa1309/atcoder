N = int(input())
tempurture = [list(map(float, input().split())) for _ in range(N)]

ans = [0] * 6

for max_tmp , min_tmp in tempurture:
    if max_tmp >= 35:
        ans[0] += 1
    if 30 <= max_tmp < 35:
        ans[1] += 1
    if 25 <= max_tmp < 30:
        ans[2] += 1
    if 25 <= min_tmp:
        ans[3] += 1
    if min_tmp < 0 and 0 <= max_tmp:
        ans[4] += 1
    if max_tmp < 0:
        ans[5] += 1
print(*ans)
