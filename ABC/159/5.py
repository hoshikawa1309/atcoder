H, W, K = map(int, input().split())
chocolates = list(list(input()) for _ in range(H))
ans = float('inf')
for i in range(2 ** (H - 1)):
    H_flag = [False] * (H - 1)
    row_cut = 0
    for j in range(H - 1):
        if i >> j & 1:
            H_flag[j] = True
            row_cut += 1

    white_chocolate = 0
    column_cut = 0
    for column in zip(chocolates):
        for i in range(len(column)):
            if column[i] == '1':
                for j in range(H - 1):
                    if white_chocolate + sum(column) >= K:
                        while_chocolate = 0
                        column_cut += sum(column)
                chocolate[i] += sum(column)
    tmp_ans = column_cut + row_cut
    if ans > tmp_ans:
        ans = tmp_ans
print(ans)
