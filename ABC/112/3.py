n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

l.sort(key=lambda x: x[2], reverse=True)
print(l)

for centerX in range(0, 101):
    for centerY in range(0, 101):
        init_X = l[0][0]
        init_Y = l[0][1]
        init_h = l[0][2]
        # ある仮中心座標と初期値のx,y,hを用いてHを仮置きする
        H = init_h + abs(init_X - centerX) + abs(init_Y - centerY)
        print(centerX, centerY, H)
        for i in range(1, n):
            x = l[i][0]
            y = l[i][1]
            h = l[i][2]
            # 全てのNについて仮置きが正しいか判定する。
            if h != max(H - abs(x - centerX) - abs(y - centerY), 0):
                break
        # for でbreakに入らなかった時実行
        else:
            print(centerX, centerY, H)
            exit()