N = input()
k = len(N)
ans = float('inf')
for i in range(1, 2 ** k):
    # 必要な変数の初期化
    tmp_ans = 0
    work = ''
    for j in range(k):  # このループが一番のポイント
        if (i >> j) & 1:  # 順に右にシフトさせ最下位bitのチェックを行う
            work += N[j]
    work = list(map(lambda x: int(x), work))
    # print(work)
    if sum(work) % 3 == 0:
        ans = min(k - len(work), ans)
if ans == float('inf'):
    print(-1)
else:
    print(ans)