N = int(input())
now_t, now_x, now_y = 0, 0, 0
for i in range(N):
    next_t, next_x, next_y = map(int, input().split())
    distance = abs(next_x - now_x) + abs(next_y - now_y)
    spent_time = next_t - now_t
    if spent_time < distance or distance % 2 != spent_time % 2:
        print('No')
        exit()
    now_t, now_x, now_y = next_t, next_x, next_y
print('Yes')
