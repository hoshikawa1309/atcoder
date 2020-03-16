bingo = []
for _ in range(3):
    row = list(map(int,input().split()))
    bingo.append(row)

N = int(input())
bingo_flag = [[False] * 3 for _ in range(3)]
for _ in range(N):
    num = int(input())
    for i in range(3):
        for j in range(3):
            if bingo[i][j] == num:
                bingo_flag[i][j] = True

# print(bingo_flag)
is_bing = False
for i in range(3):
    if bingo_flag[i][0] and bingo_flag[i][1] and bingo_flag[i][2] or \
            bingo_flag[0][i] and bingo_flag[1][i] and bingo_flag[2][i]:
        is_bing = True
        break

if bingo_flag[0][0] and bingo_flag[1][1] and bingo_flag[2][2] or \
        bingo_flag[0][2] and bingo_flag[1][1] and bingo_flag[2][0]:
    is_bing = True

if is_bing:
    print("Yes")
else:
    print("No")
