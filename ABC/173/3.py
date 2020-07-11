H, W, K = map(int, input().split())
colors = []
for _ in range(H):
    colors.append(list(input()))
black_cnt = 0
for i in range(H):
    for j in range(W):
        if colors[i][j] == '#':
            black_cnt += 1

ans = 0
for i in range(2 ** H):
    # 行方向の黒の個数を列挙
    tmp_black_cnt = black_cnt
    for j in range(H):
        if (i >> j) & 1:
            for k in range(W):
                if colors[j][k] == '#':
                    tmp_black_cnt -= 1
    # print(i, tmp_black_cnt)
    for l in range(2 ** W):
        row_tmp_black_cnt = tmp_black_cnt
        for m in range(W):
            if l == 4:
                a = 1
            if (l >> m) & 1:
                for n in range(H):
                    if colors[n][m] == '#':
                        row_tmp_black_cnt -= 1
        for j in range(H):
            for m in range(W):
                if (l >> m) & 1 and (i >> j) & 1 and colors[j][m] == '#':
                    row_tmp_black_cnt += 1
        # print(i, l, row_tmp_black_cnt)
        if row_tmp_black_cnt == K:
            ans += 1
print(ans)