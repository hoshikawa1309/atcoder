H, W, N, M = map(int, input().split())
stage = list(['.'] * W for _ in range(H))
stage_flags = list([False] * W for _ in range(H))
for _ in range(N):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    stage[a][b] = 'L'
    stage_flags[a][b] = True

for _ in range(M):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    stage[c][d] = '#'
    stage_flags[c][d] = False

for i in range(H):
    from_left_to_right = False
    from_right_to_left = False
    for j in range(W):
        if stage[i][j] == 'L':
            from_left_to_right = True
        elif from_left_to_right and stage[i][j] == '.':
            stage_flags[i][j] = True
        else:
            from_left_to_right = False

        if stage[i][W - j - 1] == 'L':
            from_right_to_left = True
        elif from_right_to_left and stage[i][W - j - 1] == '.':
            stage_flags[i][W - j - 1] = True
        else:
            from_right_to_left = False


for j in range(W):
    from_up_to_down = False
    from_down_to_up = False
    for i in range(H):
        if stage[i][j] == 'L':
            from_up_to_down = True
        elif from_up_to_down and stage[i][j] == '.':
            stage_flags[i][j] = True
        else:
            from_up_to_down = False
        if stage[H - i - 1][j] == 'L':
            from_down_to_up = True
        elif from_down_to_up and stage[H - i - 1][j] == '.':
            stage_flags[H - i - 1][j] = True
        else:
            from_down_to_up = False

ans = 0
for i in range(H):
    for j in range(W):
        if stage_flags[i][j]:
            ans += 1
print(ans)