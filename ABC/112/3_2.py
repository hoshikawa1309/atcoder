N = int(input())
pyramids = [list(map(int,input().split())) for _ in range(N)]

pyramids.sort(key=lambda x: x[2] , reverse=True)

# 仮の頂上を求めるため、最初の要素を用いる
init_X = pyramids[0][0]
init_Y = pyramids[0][1]
init_H = pyramids[0][2]
# 全探索を行う
for center_X in range(101):
    for center_Y in range(101):
        H = init_H + abs(init_X - center_X) + abs(init_Y - center_Y)
        #print(center_X , center_Y , H)
        # 最初の要素以外において、仮頂点とマンハッタン距離の関係が全て一致しているか判定
        for j in range(1,N):
            if pyramids[j][2] != max(H - abs(pyramids[j][0] - center_X) - abs(pyramids[j][1] - center_Y) , 0):
                break
        # 全て成立する時答えを出力
        else:
            print(center_X,center_Y,H)
            exit()

