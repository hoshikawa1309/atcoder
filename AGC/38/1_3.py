H, W, A, B = map(int, input().split())
ans = []
for i in range(H):
    if i < B:
       row = [1] * A
       row.extend([0] * (W - A))
    else:
        row = [0] * A
        row.extend([1] * (W - A))
    ans.append(row)
for row in ans:
    print(*row, sep='')
