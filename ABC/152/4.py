from pprint import pprint
N = int(input())
digit_cnt = list([0] * 9 for _ in range(9))
now = 1

'''
# 反省点：問題文の読み間違いをif文内で変更していなかった
for i in range(1, N + 1):
    str_i = str(i)
    if str_i[0] == "0" or str_i[-1] == "0":
        continue
    elif int(str_i[::-1]) <= N:
        #row = min(int(str_i[0]), int(str_i[-1]))
        #column = max(int(str_i[0]), int(str_i[-1]))
        row = int(str_i[0])
        column = int(str_i[-1])
        digit_cnt[row - 1][column - 1] += 1
'''
# こっちが正解
for i in range(1, N + 1):
    str_i = str(i)
    row = int(str_i[0])
    column = int(str_i[-1])
    if row != 0 and column != 0:
        digit_cnt[row - 1][column - 1] += 1
pprint(digit_cnt)

ans = 0
for i in range(9):
    for j in range(9):
        ans += digit_cnt[i][j] * digit_cnt[j][i]
print(ans)
