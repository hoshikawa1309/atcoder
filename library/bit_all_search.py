n = 10
ans = 0
for i in range(2 ** n):
    # 必要な変数の初期化
    tmp_ans = 0
    for j in range(n):  # このループが一番のポイント
        if (i >> j) & 1:  # 順に右にシフトさせ最下位bitのチェックを行う
            # ここに処理を書き込む
            pass
    ans = max(tmp_ans, ans)
print(ans)