N = int(input())
info = [[] for _ in range(N)]
people = [-1] * N
for i in range(N):
    A = int(input())
    if A == 0:
        info[i].append([0])
    for j in range(A):
        x , y = map(int,input().split())
        info[i].append([A , x - 1 , y])
#print(info[0][0][0])
ans = 0
# ビット全探索を行う
for i in range(2 ** N):
    cnt = 0
    Flag = True
    # ビットが１の時、正直者としてpeopleに格納
    for j in range(N):
        if i >> j & 1:
            cnt += 1
            people[j] = 1
        else:
            people[j] = 0
    for j in range(N):
        # 正直者の発言と実際に正直者であるかを判定
        if i >> j & 1:
            info_num = info[j][0][0]
            for k in range(info_num):
                judge = info[j][k][2]
                origin = people[info[j][k][1]]
                if judge != origin:
                    Flag = False
                    break
        if not Flag:
            break
    if Flag:
        if ans < cnt:
            ans = cnt
print(ans)

