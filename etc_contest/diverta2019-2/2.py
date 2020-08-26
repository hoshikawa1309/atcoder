N = int(input())
balls = []
for _ in range(N):
    balls.append(list(map(int, input().split())))

if N <= 2:
    print(1)
    exit()
ans = float('inf')
for i in range(N - 2):
    x1, y1 = balls[i]
    ball_flags = [False] * N
    ball_flags[i] = True
    tmp_ans = 0
    for j in range(i + 1, N - 1):
        x2, y2 = balls[j]
        ball_flags[j] = True
        while not all(ball_flags):
            tmp_ans += 1
            tmp_x1, tmp_y1 = float('inf'), float('inf')
            tmp_x2, tmp_y2 = float('inf'), float('inf')
            for k in range(N):
                if ball_flags[k]:
                    continue
                x, y = balls[k]
                if (y - y1) * (x2 - x1) == (y2 - y1) * (x - x1):
                    ball_flags[k] = True
                else:
                    if tmp_x1 == float('inf'):
                        tmp_x1, tmp_y1 = x, y
                        idx1 = k
                    if tmp_x2 == float('inf'):
                        tmp_x2, tmp_y2 = x, y
                        idx2 = k
            if all(ball_flags):
                break
            elif sum(ball_flags) == N - 1:
                tmp_ans += 1
                break
            else:
                x1, x2 = tmp_x1, tmp_x2
                ball_flags[idx1] = True
                y1, y2 = tmp_y1, tmp_y2
                ball_flags[idx2] = True
        ans = min(tmp_ans, ans)
print(ans)